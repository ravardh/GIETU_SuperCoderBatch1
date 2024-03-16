operation = input("+ for addition -for subtraction *for multiplication/ for division")
number_1 = float(input('Enter 1st num: '))
number_2 = float(input('Enter  2nd num: '))

if operation == '+':
    print(number_1 + number_2)

elif operation == '-':
    print(number_1 - number_2)

elif operation == '*':
    print(number_1 * number_2)

elif operation == '/':
    
    if number_2 != 0:
        print(number_1 / number_2)
    else:
        print("You can't divide by zero!")