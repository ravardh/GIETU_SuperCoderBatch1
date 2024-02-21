 def bubble_sort(arr):
     n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
             if arr[j]>arr[j+1]:
                 arr[j],arr[j+1]=arr[j+1],arr[j]
     return arr
 print(bubble_sort([30,40,10,20]))



x=2
y=4
#x=4
#y=2
x,y=y,x
print(x,y)
