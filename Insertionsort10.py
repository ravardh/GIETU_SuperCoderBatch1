def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr = eval(input("Enter a list of elements for sorting (separated by spaces): "))
insertionSort(arr)
print("After Sorting:", arr)
