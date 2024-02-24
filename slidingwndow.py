#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#sliding window technique(without slicing)
l=list(map(int,input("Enter list numbers: ").split()))
l2=[]
sum=0
m=int(input("Enter a number smaller than length of list: "))
n=m
for i in range(len(l)-m+1):
    while(m>0):
        sum+=l[i]
        i+=1
        m-=1
    l2.append(sum)
    sum=0
    m=n
print(max(l2))

