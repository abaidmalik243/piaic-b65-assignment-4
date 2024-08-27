# Q - 04
# Write a program that calculates the area of the cube.

# Surface Area = 6 × side^2

# Function to calculate the surface area of a cube
def calculate_cube_surface_area(side):
    return 6 * (side ** 2)

# Example usage
side = float(input("Enter the length of a side of the cube: "))

surface_area = calculate_cube_surface_area(side)
print(f"The surface area of the cube is: {surface_area:.2f} square units.")