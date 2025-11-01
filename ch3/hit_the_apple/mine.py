#9 Simple calculator: Create a simple calculator in Python 
# that can add, subtract, multiply, and divide two numbers.
# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main program
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = input("Enter first single-digit number (0-9): ")
        num2 = input("Enter second single-digit number (0-9): ")

        # Check if inputs are single digits
        if num1.isdigit() and num2.isdigit() and 0 <= int(num1) <= 9 and 0 <= int(num2) <= 9:
            num1 = int(num1)
            num2 = int(num2)

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid input! Please enter single-digit numbers only.")
    else:
        print("Invalid choice! Please enter a valid operation number.")

# Run the calculator
calculator()