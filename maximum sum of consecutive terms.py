#!/usr/bin/env python
# coding: utf-8

# In[3]:


def max_sum_of_triplets(arr, num_terms_to_sum):
    max_sum = float('-inf') 
    max_triplet = None  
    
    
    for i in range(len(arr) - num_terms_to_sum + 1):
        
        terms_sum = sum(arr[i:i+num_terms_to_sum])
        
        
        if terms_sum > max_sum:
            max_sum = terms_sum
            max_triplet = tuple(arr[i:i+num_terms_to_sum])  
    
    return max_sum, max_triplet


num_terms_total = int(input("Enter the total number of terms in the array: "))
array = []


for i in range(num_terms_total):
    term = int(input(f"Enter term {i + 1}: "))
    array.append(term)


num_terms_to_sum = int(input("Enter the number of terms to consider for sum: "))


max_sum, max_terms = max_sum_of_triplets(array, num_terms_to_sum)

print("Maximum sum of terms:", max_sum)
print("Terms with maximum sum:", max_terms)


# In[ ]:




