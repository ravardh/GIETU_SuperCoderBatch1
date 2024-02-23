#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Bubble_sort
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
data=[3,12,54,11,6,23,15]
bubbleSort(data)
print("The Sorted array is",data)


# In[8]:


#Insertion_sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [11, 15, 10, 67, 90, 22, 21]
insertion_sort(arr)
print("Insertion Sort:", arr)


# In[1]:


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [4, 7, 8, 1, 9, 2, 3, 6, 5]
selection_sort(arr)
print("Selection Sort:", arr)


# In[ ]:




