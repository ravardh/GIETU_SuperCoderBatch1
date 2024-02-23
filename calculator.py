a=int(input())
b=int(input())
op=input("enter the operator")
match op:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case "%":
        print(a%b) 
    case "//":
        print(a//b)
    case "^":
        print(a**b)
    case _:
        print("Invalid Operator")