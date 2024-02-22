#!/usr/bin/env python
# coding: utf-8

# In[11]:


def calculator(operator,num1,num2):
    match operator:
        case '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        case '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        case '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero!")
        case '%' :
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
        case _:
            print("Invalid operator")
            
calculator("+",7,10 )
calculator("-", 13, 3)
calculator("*", 10, 55)
calculator("/", 10, 5)
calculator("%", 13, 6)
calculator("//",5,8)
        


# In[ ]:




