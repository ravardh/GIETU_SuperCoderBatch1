def partition(arr, start, end):
    j = start - 1
    ele = arr[end]
    for i in range(start, end):
        if arr[i] <= ele:
            j = j + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[j + 1], arr[end]= arr[end], arr[j + 1]
    return j + 1

def quickSort(arr, start, end):
    if start < end:
        pidx = partition(arr, start, end)
        quickSort(arr, start, pidx - 1)
        quickSort(arr, pidx + 1, end)

n = eval(input("Enter a list of elements for sorting: "))
quickSort(n, 0, len(n) - 1)
print("After Sorting:", n)