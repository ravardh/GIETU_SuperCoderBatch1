def mergeSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    i = low
    j = mid + 1
    k = low
    arr1 = []

    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            arr1.append(arr[i])
            i = i + 1
        else:
            arr1.append(arr[j])
            j = j + 1

    while i <= mid:
        arr1.append(arr[i])
        i = i + 1

    while j <= high:
        arr1.append(arr[j])
        j = j + 1

    for i in range(len(arr1)):
        arr[low + i] = arr1[i]


arr = eval(input("Enter a list of elements for sorting: "))
mergeSort(arr, 0, len(arr) - 1)
print("After Sorting:", arr)
