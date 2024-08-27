# Q - 03
# Write a program that calculates the area of a circle.

import math

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

# Example usage
radius = float(input("Enter the radius of the circle: "))

area = calculate_circle_area(radius)
print(f"The area of the circle is: {area:.2f} square units.")