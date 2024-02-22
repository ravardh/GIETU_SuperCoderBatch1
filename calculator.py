x=int(input("Enter first number"))
op=input("Enter operator")
op=op.lower()
y=int(input("Enter second number"))
match op:
    case '+':
        print(x+y)
    case '-':
        print(x-y)
    case '*':
        print(x*y)
    case '/':
        print(x/y)
    case '%':
        print(x%y)
    case '^':
        print(x**y)
    case 'sqrt':
        print(x**(1/2))
    case _:
        print("Invalid operator")