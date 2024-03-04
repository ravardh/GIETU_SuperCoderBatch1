# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 08:54:35 2024

@author: HP
"""

lst = eval(input("Enter a list:"))
pattern = eval(input("Enter pattern:"))

n = len(pattern)
indices = []

for i in range(len(lst) - n + 1):
    if lst[i:i+n] == pattern:
        indices.append(i)

if indices:
    print(f"The pattern {pattern} is found at indices: {indices}")
else:
    print("Pattern not found in the list.")
