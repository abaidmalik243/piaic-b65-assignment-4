# Q - 02
# Write a program that calculates the area of a rectangle using length and width variables.

# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Example usage
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate_area(length, width)
print(f"The area of the rectangle is: {area} square units.")