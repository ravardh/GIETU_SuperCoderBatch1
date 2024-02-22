num1=int(input("num1 : "))
num2=int(input("num2 : "))
operator=input("operator : ")
match operator:
  case '+':
    print(num1+num2)
  case '-':
    print(num1-num2)
  case '*':
    print(num1*num2)
  case '/':
    print(num1/num2)
  case '//':
    print(num1//num2)
  case '%':
    print(num1%num2)
  case _:
    print("invalid operator")