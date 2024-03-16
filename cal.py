def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def main():
    print("Please select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    select = int(input("Select operation (1/2/3/4): "))
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))

    if select == 1:
        print(f"{number_1} + {number_2} =", add(number_1, number_2))
    elif select == 2:
        print(f"{number_1} - {number_2} =", subtract(number_1, number_2))
    elif select == 3:
        print(f"{number_1} * {number_2} =", multiply(number_1, number_2))
    elif select == 4:
        print(f"{number_1} / {number_2} =", divide(number_1, number_2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
