#!/usr/bin/env python
# coding: utf-8

# In[1]:


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
arr = [4, 7, 8, 1, 9, 2, 3, 6, 5]
selection_sort(arr)
print("Sorted array:", arr)


# In[ ]:




