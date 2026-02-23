# Write a program find out addition, difference, product and division of two numbers by creating, a user defined function.

def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation"
'''
# Example usage:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (add/subtract/multiply/divide): ")

result = calculate(num1, num2, operation)
print(f"Result: {result}")'''