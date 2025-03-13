"""Basic Calculator Program

Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15."""

# Getting user's number
# Getting user's number
input1  = input("Input the first number: ")
input2 = input("Input the second number: ")
operator = input("Input the operator (+, -, *, /): ")

# Convert inputs to float
num1 = float(input1)
num2 = float(input2)

# Perform the operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

# Print the result
print(f"The result of {num1} {operator} {num2} is: {result}")