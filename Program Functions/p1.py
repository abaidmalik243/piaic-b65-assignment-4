# Q - 01
# Calculate your age based on the current year and your birth year.

from datetime import datetime

# Function to calculate age
def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

# Example usage
birth_year = int(input("Enter your birth year: "))
age = calculate_age(birth_year)
print(f"You are {age} years old.")
