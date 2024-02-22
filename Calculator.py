x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
op=input("Enter operator: ")
match op:
    case '+':
        print(x+y)
    case '-':
        print(x-y)
    case '*':
        print(x*y)
    case '/':
        print(x/y)
    case '//':
        print(x//y)
    case '%':
        print(x%y)
    case '^':
        print(x**y)
    case _:
        print("Invalid operator")