# Q - 06
# Convert a given number of seconds into minutes and seconds using variables.

# Function to convert seconds into minutes and seconds
def convert_seconds(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return minutes, seconds

# Example usage
total_seconds = int(input("Enter the number of seconds: "))

minutes, seconds = convert_seconds(total_seconds)
print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")
