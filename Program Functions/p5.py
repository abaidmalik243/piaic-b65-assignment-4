# Q - 05
# Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

# Example usage
temperature = float(input("Enter the temperature: "))
unit = input("Is this temperature in Fahrenheit (F) or Celsius (C)? Enter F or C: ").strip().upper()

if unit == 'F':
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature}° Fahrenheit is equal to {converted_temperature:.2f}° Celsius.")
elif unit == 'C':
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature}° Celsius is equal to {converted_temperature:.2f}° Fahrenheit.")
else:
    print("Invalid input! Please enter 'F' for Fahrenheit or 'C' for Celsius.")
