import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
import numpy as np
from PIL import Image, ImageDraw
import random


# Function to generate synthetic circle images
def generate_circle_image(image_size=64):
    image = Image.new("L", (image_size, image_size), color=0)  # Create a new grayscale image with a black background.
    draw = ImageDraw.Draw(image)  # Create a drawing object.
    radius = random.randint(10, image_size // 3)  # Pick a random radius.
    x0 = random.randint(radius, image_size - radius)  # Random x-coordinate ensuring the circle fits.
    y0 = random.randint(radius, image_size - radius)  # Random y-coordinate ensuring the circle fits.
    bounding_box = [(x0 - radius, y0 - radius), (x0 + radius, y0 + radius)]  # Define the circle bounding box.
    draw.ellipse(bounding_box, fill=255)  # Draw a white circle.
    return np.array(image)  # Return the image as a NumPy array.


# Function to generate synthetic rectangle images
def generate_rectangle_image(image_size=64):
    image = Image.new("L", (image_size, image_size), color=0)  # Create a new grayscale image with black background.
    draw = ImageDraw.Draw(image)  # Create a drawing object.
    rect_width = random.randint(10, image_size // 2)  # Random rectangle width.
    rect_height = random.randint(10, image_size // 2)  # Random rectangle height.
    x0 = random.randint(0, image_size - rect_width)  # Random x-coordinate.
    y0 = random.randint(0, image_size - rect_height)  # Random y-coordinate.
    bounding_box = [x0, y0, x0 + rect_width, y0 + rect_height]  # Define the rectangle bounding box.
    draw.rectangle(bounding_box, fill=255)  # Draw a white rectangle.
    return np.array(image)  # Return the image as a NumPy array.


# Custom dataset for our shapes
class ShapeDataset(Dataset):
    def __init__(self, num_samples_per_class, image_size=64):
        self.images = []
        self.labels = []
        # Generate circle images; label 0 = circle.
        for _ in range(num_samples_per_class):
            self.images.append(generate_circle_image(image_size))
            self.labels.append(0)
        # Generate rectangle images; label 1 = rectangle.
        for _ in range(num_samples_per_class):
            self.images.append(generate_rectangle_image(image_size))
            self.labels.append(1)

        # Convert lists to NumPy arrays and normalize pixel values to the range [0, 1].
        self.images = np.array(self.images).astype("float32") / 255.0
        self.labels = np.array(self.labels)

    def __len__(self):
        return len(self.images)  # Return the total number of images.

    def __getitem__(self, idx):
        image = self.images[idx].reshape(1, 64, 64)  # Reshape to (channel, height, width) for PyTorch.
        label = self.labels[idx]
        return torch.tensor(image), torch.tensor(label)  # Return tensors for both image and label.


# Create dataset instance and split it into training and testing sets.
dataset = ShapeDataset(num_samples_per_class=500, image_size=64)
train_size = int(len(dataset) * 0.8)  # Use 80% of the data for training.
test_size = len(dataset) - train_size  # Remaining 20% for testing.
train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, test_size])

# Create DataLoaders for batching the data.
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)


# Define the CNN model using PyTorch's nn.Module.
class ShapeCNN(nn.Module):
    def __init__(self):
        super(ShapeCNN, self).__init__()
        # First convolutional layer: in_channels=1 (grayscale), out_channels=32; kernel_size=3 and padding to preserve size.
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.relu1 = nn.ReLU()  # ReLU activation introduces non-linearity.
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)  # Downsample by a factor of 2.

        # Second convolutional layer: in_channels=32 from the previous layer, out_channels=64.
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)

        # Fully connected layer. The feature maps are now 64 channels of 16x16 (64 divided by 2 twice).
        self.fc1 = nn.Linear(64 * 16 * 16, 64)
        self.relu3 = nn.ReLU()
        # Final output layer: single neuron that outputs a value for binary classification.
        self.fc2 = nn.Linear(64, 1)
        self.sigmoid = nn.Sigmoid()  # Sigmoid activation squashes outputs to [0, 1].

    def forward(self, x):
        x = self.conv1(x)  # Apply first convolution.
        x = self.relu1(x)  # Apply ReLU activation.
        x = self.pool1(x)  # Downsample.

        x = self.conv2(x)  # Apply second convolution.
        x = self.relu2(x)  # Apply ReLU activation.
        x = self.pool2(x)  # Downsample further.

        x = x.view(x.size(0), -1)  # Flatten the feature maps to a 1D vector for each example.
        x = self.fc1(x)  # Fully connected layer.
        x = self.relu3(x)  # Apply ReLU.
        x = self.fc2(x)  # Final linear layer.
        x = self.sigmoid(x)  # Sigmoid activation to get probability between 0 and 1.
        return x


# Instantiate the model.
model = ShapeCNN()

# Define the loss function (binary cross-entropy loss for binary classification).
criterion = nn.BCELoss()
# Define the optimizer: Adam optimizer with learning rate of 0.001.
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training loop for the model.
epochs = 10
for epoch in range(epochs):
    running_loss = 0.0
    for images, labels in train_loader:
        outputs = model(images)  # Forward pass: compute the output of the model.
        outputs = outputs.squeeze()  # Remove extra dimensions if present.
        loss = criterion(outputs, labels.float())  # Compute the loss comparing outputs and true labels.

        optimizer.zero_grad()  # Zero the gradients from the previous iteration.
        loss.backward()  # Backward pass: compute gradients with respect to model parameters.
        optimizer.step()  # Update the model parameters according to the optimizer.

        running_loss += loss.item()  # Accumulate the training loss.

    print(f"Epoch {epoch + 1}/{epochs}, Loss: {running_loss / len(train_loader):.4f}")

# Evaluating the model on the test set.
model.eval()  # Set the model to evaluation mode.
correct = 0
total = 0
with torch.no_grad():  # Turn off gradient calculation for evaluation.
    for images, labels in test_loader:
        outputs = model(images).squeeze()  # Get model predictions.
        predicted = (
                    outputs > 0.5).long()  # Apply threshold: if output > 0.5, classify as 1 (rectangle); else 0 (circle).
        total += labels.size(0)
        correct += (predicted == labels).sum().item()  # Count correct predictions.

print(f"Test Accuracy: {100 * correct / total:.2f}%")
# ... [model definition and training code]
torch.save(model.state_dict(), "shape_cnn.pth")