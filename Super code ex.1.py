# Calculator
A=int(input("Input Number:"))
B=int(input("Input Number:"))
Ch=input("Enter your choice:")
match Ch:
    case '+':
        print(A+B)
    case '-':
        print(A-B)
    case '*':
        print(A*B)
    case '/':
        print(A/B)
    case '_':
        print("worng input")
