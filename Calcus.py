op=input("Enter the operator=")
a=int(input("Enter for a="))
b=int(input("enter for b="))
if(op == "*"):
    print(a*b)
elif(op == "+"):
    print(a+b)
elif(op == "/"):
    print(a/b)
elif(op == "//"):
    print(a//b)
else:
    print("Invalid operator")