# Q - 07
# Write a program that calculates the percentage.

# Function to calculate the percentage
def calculate_percentage(value, total):
    return (value / total) * 100

# Percentage = (Total Value) × 100

# Example usage
value = float(input("Enter the obtained value: "))
total = float(input("Enter the total value: "))

if total != 0:
    percentage = calculate_percentage(value, total)
    print(f"The percentage is: {percentage:.2f}%")
else:
    print("The total value cannot be zero.")
