import sys

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

# Check if command-line arguments are provided
if len(sys.argv) != 4:
    print("Usage: python3 main.py <operation> <number1> <number2>")
    sys.exit(1)

# Parse command-line arguments
select = int(sys.argv[1])
number_1 = int(sys.argv[2])
number_2 = int(sys.argv[3])

# Perform the selected operation
if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))
elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))
else:
    print("Invalid input")
