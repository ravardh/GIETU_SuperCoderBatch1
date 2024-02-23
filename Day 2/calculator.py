'''Approach 1:
print(eval(input()))
'''

'''Approach 2:
a = input("Enter 1st num: ")
b = input("Enter 1st num: ")
op = input("Enter Operator: ")
print(eval(f'{a}{op}{b}'))
'''

# Approach 3
s,operand,operator='','',''
print("Enter = to stop the input")
while(operator != '='):
  operand,operator=input("Enter Operand: "),input("Enter Operator: ")
  s+=((operand+operator).strip())
  print(f'Current Equation: {s}?')
print(f'Equation: {s}{eval(s[:-1])}')
