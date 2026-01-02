# pattern_drawing.py
# Objective: Draw a square pattern of asterisks using a while loop and a nested for loop.

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to iterate through rows
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")  # Print asterisk without moving to a new line
    print()  # Move to the next line after finishing the row
    row += 1

