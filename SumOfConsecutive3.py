# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 09:55:38 2024

@author: HP
"""

def max_sum(arr):
    if len(arr) < 3:
        return "List should have at least 3 elements"
    
    max_sum = 0 
    
    for i in range(len(arr) - 2):
        current_sum = arr[i] + arr[i + 1] + arr[i + 2]
        if current_sum > max_sum:
            max_sum = current_sum
  
    return max_sum


arr = eval(input("Enter a list:"))
result = max_sum(arr)
print("Maximum sum:", result)

