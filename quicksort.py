list = [4,7,8,1,9,2,3,6,5]

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j] <= pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quicksort(arr,low,high):
    if low<high:
        x=partition(arr,low,high)
        quicksort(arr,low,x-1)
        quicksort(arr,x+1,high)
    return arr
n=len(list)
print(quicksort(list, 0, n-1))