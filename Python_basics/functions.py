import math

def calculate_area(shape, dimension1, dimension2=0):
  
    shape = shape.lower()  

    if shape == "circle":
        radius = dimension1
        return math.pi * radius**2
    elif shape == "rectangle":
        length = dimension1
        width = dimension2
        return length * width
    elif shape == "triangle":
        base = dimension1
        height = dimension2
        return 0.5 * base * height
    else:
        return "Invalid shape. Please choose from 'circle', 'rectangle', or 'triangle'."