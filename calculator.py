def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

def calculator(operation, x, y):
    match operation:
        case 'add':
            return add(x, y)
        case 'subtract':
            return subtract(x, y)
        case 'multiply':
            return multiply(x, y)
        case 'divide':
            return divide(x, y)
        case _:
            return "Invalid operation!"

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            operation = 'add'
        elif choice == '2':
            operation = 'subtract'
        elif choice == '3':
            operation = 'multiply'
        elif choice == '4':
            operation = 'divide'

        result = calculator(operation, num1, num2)
        print("Result:", result)
    else:
        print("Invalid Input")

    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() == 'no':
        break
