def Insertation(arr):
    n=len(arr)
    for i in range(1,n):
        j=i
        while j>0 and arr[j-1] >arr[j]:
            arr[j], arr[j-1] = arr[j-1],arr[j]
            j=j-1
    return arr
arr = [30,40,10,20]
Insertation(arr)
print(arr)
