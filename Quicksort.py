def quickSort(arr, start, end):
    if start < end:
        pivot = arr[end]
        i = start - 1
        for j in range(start, end):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        
        quickSort(arr, start, i)
        quickSort(arr, i + 2, end)

    return arr

arr = [1, 6, 4, 8, 6, 3, 9, 5]
end = len(arr)
quickSort(arr, 0, end - 1)
print("The Sorted array is:" )
for x in arr:
    print(x, end=" ")
          