arr = [ 7,9,8,10,5,4]
def bubbleSort(arr):
    for i in range (len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
print(arr)
bubbleSort(arr)
print("Sorted array is")
for i in range(len(arr)):
    print("%d" %arr[i] , end= " ")
                   
                   
                   
                   