x=int(input("Enter first number"))
y=int(input("Enter second number"))
op=input("Enter Operstor")

match op:
    case '+':
        print (x+y)
    case '-':
        print (x-y)
    case '*':
        print (x*y)
    case '/':
        print (x/y)
    case '%':
        print (x%y)
    case '//':
        print (x//y)
