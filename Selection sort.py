#!/usr/bin/env python
# coding: utf-8

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




