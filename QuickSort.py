# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:45:31 2024

@author: HP
"""

def find(arr,s,e):
    p=arr[e]
    j=s-1
    for i in range(s,e):
        if arr[i]<p:
            j=j+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[j+1],arr[e]=arr[e],arr[j+1]
    return j+1

def quick(arr,s,e):
    if s<e:
        pi=find(arr,s,e)
        quick(arr,s,pi-1)
        quick(arr,pi+1,e)
if __name__ =='_main_':
    arr=eval(input("Enter a list:"))
    quick(arr,0,len(arr)-1)
    print (arr)