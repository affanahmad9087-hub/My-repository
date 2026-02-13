import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
import numpy as np
from PIL import Image, ImageDraw
import random

image_size = 64

image = Image.new("L", (image_size, image_size), color=0)  # Create a new grayscale image with a black background.
draw = ImageDraw.Draw(image)  # Create a drawing object.
radius = random.randint(10, image_size // 3)  # Pick a random radius.
x0 = random.randint(radius, image_size - radius)  # Random x-coordinate ensuring the circle fits.
y0 = random.randint(radius, image_size - radius)  # Random y-coordinate ensuring the circle fits.
bounding_box = [(x0 - radius, y0 - radius), (x0 + radius, y0 + radius)]  # Define the circle bounding box.
draw.ellipse(bounding_box, fill=255)  # Draw a white circle.

image.save("Circle/circle.png", format = "PNG")

image = Image.new("L", (image_size, image_size), color=0)  # Create a new grayscale image with black background.
draw = ImageDraw.Draw(image)  # Create a drawing object.
rect_width = random.randint(10, image_size // 2)  # Random rectangle width.
rect_height = random.randint(10, image_size // 2)  # Random rectangle height.
x0 = random.randint(0, image_size - rect_width)  # Random x-coordinate.
y0 = random.randint(0, image_size - rect_height)  # Random y-coordinate.
bounding_box = [x0, y0, x0 + rect_width, y0 + rect_height]  # Define the rectangle bounding box.
draw.rectangle(bounding_box, fill=255)  # Draw a white rectangle.

image.save("Rectangle/rect.png", format = "PNG")