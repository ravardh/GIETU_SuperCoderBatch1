x= int(input("Enter first number"))
y= int(input("Enter second umber"))
op= input("Enter Operator")

match op:
    case '+' :
        print (x+y)
    case '-' :
        print (x-y)
    case '*' :
        print (x*y)
    case '/' :
        print (x/y)
    case '%' :
        print (x%y)
    case '//' :
        print (x//y)
