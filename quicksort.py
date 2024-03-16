def partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

def quicksort(arr, low, high):
    if low < high:
        split_index = partition(arr, low, high)
        quicksort(arr, low, split_index)
        quicksort(arr, split_index + 1, high)


arr = [29, 10, 14, 37, 13]
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
