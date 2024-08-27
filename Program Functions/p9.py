# Q - 09
# Write a program that calculates the volume of a cylinder using the formula.

# Volume = π × radius^2 ×height
import math

# Function to calculate the volume of a cylinder
def calculate_cylinder_volume(radius, height):
    return math.pi * (radius ** 2) * height

# Example usage
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = calculate_cylinder_volume(radius, height)
print(f"The volume of the cylinder is: {volume:.2f} cubic units.")