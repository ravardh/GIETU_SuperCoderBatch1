operation = input("+ for addition -for subtraction *for multiplication/ for division")
a = float(input('Enter 1st num: '))
b = float(input('Enter  2nd num: '))

if operation == '+':
    print(a+b)

elif operation == '-':
    print(a-b)

elif operation == '*':
    print(a * b)
elif operation == '/':   
    if b != 0:
        print(a/b)
    else:
        print("You can't divide by zero!")
