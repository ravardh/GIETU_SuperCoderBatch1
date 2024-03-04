#bubble sorting
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [4, 7, 8, 1, 9, 2, 3, 6, 5]
bubble_sort(arr)
print("Bubble Sort:", arr)

#selection sorting
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [4, 7, 8, 1, 9, 2, 3, 6, 5]
selection_sort(arr)
print("Selection Sort:", arr)

#insertion sorting 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [4, 7, 8, 1, 9, 2, 3, 6, 5]
insertion_sort(arr)
print("Insertion Sort:", arr)

