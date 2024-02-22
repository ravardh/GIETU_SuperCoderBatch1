a=float(input("enter the 1st number"))
b=float(input("enter the 2nd number"))

print("Simple Calculator")
print("Menu:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")
if choice == '1':
    result = a + b
    print("Result:", result)
elif choice == '2':
    result = a - b
    print("Result:", result)
elif choice == '3':
    result = a * b
    print("Result:", result)
elif choice == '4':
    if b == 0:
        print("Error! Division by zero.")
    else:
        result = a / b
        print("Result:", result)
else:
    print("Invalid Input")