op=input("Enter the operator")
num1=int(input())
num2=int(input())
if(op== '+'):
    print(num1+num2)
elif(op== '-'):
    print(num1-num2)
elif(op== '*'):
    print(num1*num2)
elif(op== '/'):
    print(num1/num2)
elif(op=='//'):
    print(num1//num2)
elif(op=='**'):
    print(num1**num2)
else:
    print("Invalid operator")