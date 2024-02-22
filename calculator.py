def calculator(operator, num1, num2):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "Cannot divide by zero"
        case _:
            return "Invalid operator"

# Test the calculator
Operator = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = calculator(operator, num1, num2)
print("Result:", result)
