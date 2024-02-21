a=int(input("enter the first number:"))
b=int(input("enter the second number:"))

operator=input("enter the operator:")

match operator:
    case'+':
        print(a+b)
    case'-':
        print(a-b)
    case'*':
        print(a*b)
    case'/':
        print(a/b)
    case'%':
        print(a%b)