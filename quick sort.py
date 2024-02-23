#!/usr/bin/env python
# coding: utf-8

# In[1]:


def partition(arr,start,end):
    pivot=arr[end]
    j=start-1
    for i in  range(start,end):
        if arr[i]<=pivot:
            j=j+1
            arr[j],arr[i]=arr[i],arr[j]
    arr[j+1],arr[end]=arr[end],arr[j+1]
    return j+1
    
def quicksort(arr,start,end):
    if start<end:
        pi=partition(arr,start,end)
        quicksort(arr,start,pi-1)
        quicksort(arr,pi+1,end)
    
if __name__ == '__main__':
    arr=[3,7,4,5,1,2,9,10,8]
    quicksort(arr,0,len(arr)-1)
    print(arr)


# In[ ]:




