# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:39:01 2024

@author: HP
"""

#BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = eval(input("Enter an array"))
bubble_sort(arr)
print("Sorted array is:", arr)

#SELECTION SORT
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = eval(input("Enter an array"))
selection_sort(arr)
print("Sorted array is:", arr)

#INSERTION SORT
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = eval(input("Enter an array"))
insertion_sort(arr)
print("Sorted array is:", arr)


