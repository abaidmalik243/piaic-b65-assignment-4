# Q - 08
# Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Example usage
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")

# Optional: Provide BMI category based on the calculated BMI
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")