op=input("Enter the operator=")
a=int(input("Enter for a="))
b=int(input("enter for b="))
match op:
    case "*":
         print(a*b)
    case "+":
        print(a+b)
    case "/":
        print(a/b)
    case "//":
        print(a//b)
    case _:
        print("Invalid operator")