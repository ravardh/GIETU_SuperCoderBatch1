# simple calculator

num1 = int(input())
num2= int(input())
op = input()
match op:
  case "+":
    print(num1 + num2)
  case "-":
    print(num1 - num2)
  case "*":
    print(num1 * num2)
  case "/":
    print(num1 / num2)
  case _:
    print("Invalid operator")
