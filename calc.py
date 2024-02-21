#calculator
num1=int(input("Enter the first number:\n"))
num2=int(input("Enter the second number:\n"))
choice=True
while(choice==True):
    print("Enter the operation to perform:addition-a,subtraction-s,multiplication-m:\n")
    ch=input("Enter the operation to perform:\n")
    match ch:
        case 'a':
            print(num1+num2)
        case 's':
            print(num1-num2)
        case 'm':
            print(num1*num2)
        case _:
            print("invalid operation")
    print("Do you wanna go further?T or F:\n")
    var=input("Enter T or F:\n")
    if(var=='T'):
        choice=True
    elif(var=='F'):
        choice=False