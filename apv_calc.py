import math

def calculate_area(shape):
    if shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius ** 2
        return area
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        return area
    elif shape == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        return area
    elif shape == "square":
        side = float(input("Enter the side length of the square: "))
        area = side ** 2
        return area
    elif shape == "cylinder":
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        area = 2 * math.pi * radius * (radius + height)
        return area
    else:
        return "Invalid shape"

def calculate_perimeter(shape):
    if shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        perimeter = 2 * math.pi * radius
        return perimeter
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        perimeter = 2 * (length + width)
        return perimeter
    elif shape == "triangle":
        side1 = float(input("Enter the length of side 1 of the triangle: "))
        side2 = float(input("Enter the length of side 2 of the triangle: "))
        side3 = float(input("Enter the length of side 3 of the triangle: "))
        perimeter = side1 + side2 + side3
        return perimeter
    elif shape == "square":
        side = float(input("Enter the side length of the square: "))
        perimeter = 4 * side
        return perimeter
    elif shape == "cylinder":
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        perimeter = 2 * math.pi * radius + 2 * height
        return perimeter
    else:
        return "Invalid shape"
    
def calculate_volume(shape):
    if shape == "cylinder":
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        volume = math.pi * radius ** 2 * height
        return volume
    else:
        return "Volume calculation is only available for cylinders."
    