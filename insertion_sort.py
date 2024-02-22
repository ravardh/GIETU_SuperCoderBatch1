def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j= i-1
        while j >=0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = temp
    return arr
arr = [ 8,7,9,5,4]
print("the sorted list :",insertionSort(arr))
