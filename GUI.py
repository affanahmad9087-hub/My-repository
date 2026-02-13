import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torch.optim import Adam

# Import your model components from model.py
# Replace 'model' with the actual name of your module file without the .py extension.
from model import ShapeCNN, ShapeDataset, preprocess_image


class MLApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interactive ML GUI")
        self.geometry("700x500")

        # Create GUI elements
        self.create_widgets()

        # Initialize your model, loss function, and optimizer.
        # (Adjust hyperparameters, learning rates, etc., as needed.)
        self.model = ShapeCNN()
        self.criterion = nn.BCELoss()
        self.optimizer = Adam(self.model.parameters(), lr=0.001)

    def create_widgets(self):
        # Button to start training
        self.train_btn = tk.Button(self, text="Train Model", command=self.start_training)
        self.train_btn.pack(pady=10)

        # Button to start testing
        self.test_btn = tk.Button(self, text="Test Model", command=self.test_model)
        self.test_btn.pack(pady=10)

        # Scrolled text area to show log messages
        self.log_area = scrolledtext.ScrolledText(self, width=85, height=20)
        self.log_area.pack(pady=10)

    def log(self, message):
        """Helper method to insert a log message into the text area."""
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)

    def start_training(self):
        """Start the training process on a separate thread."""
        training_thread = threading.Thread(target=self.train_model)
        training_thread.start()

    def train_model(self):
        self.log("Training started...")

        # Create your dataset; here we assume 500 samples per class
        dataset = ShapeDataset(num_samples_per_class=500, image_size=64)
        train_size = int(len(dataset) * 0.8)
        train_dataset, _ = torch.utils.data.random_split(dataset, [train_size, len(dataset) - train_size])
        train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

        epochs = 10
        for epoch in range(epochs):
            running_loss = 0.0
            for images, labels in train_loader:
                outputs = self.model(images)
                outputs = outputs.squeeze()
                loss = self.criterion(outputs, labels.float())

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                running_loss += loss.item()
            avg_loss = running_loss / len(train_loader)
            self.log(f"Epoch {epoch + 1}/{epochs}, Loss: {avg_loss:.4f}")

        self.log("Training finished!")
        # Optionally save the model after training
        torch.save(self.model.state_dict(), "shape_cnn.pth")
        self.log("Model saved to shape_cnn.pth.")

    def test_model(self):
        """Open a file dialog to select an image for testing and then process it."""
        file_path = filedialog.askopenfilename(
            title="Select Test Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        if file_path:
            self.log(f"Testing image: {file_path}")
            try:
                # Preprocess the image and generate a tensor
                img_tensor = preprocess_image(file_path, image_size=64)
                self.model.eval()  # Set the model to evaluation mode
                with torch.no_grad():
                    output = self.model(img_tensor).squeeze()
                    prediction = output.item()
                    class_label = "Rectangle (1)" if prediction > 0.5 else "Circle (0)"
                self.log(f"Prediction value: {prediction:.4f}")
                self.log(f"Classified as: {class_label}")
                messagebox.showinfo("Test Result", f"Prediction value: {prediction:.4f}\nClassified as: {class_label}")
            except Exception as e:
                self.log("Error during testing: " + str(e))
                messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = MLApp()
    app.mainloop()