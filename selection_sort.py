# Selection Sort

def selection_sort(arr):
  for i in range(len(arr)):
    min_id = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_id]:
        min_id = j
    arr[i], arr[min_id] = arr[min_id], arr[i]
  return arr

# arr = [34,23,12,93,6,48,7,6]
arr = list(map(int, input().split()))  
print("The unsorted array is:", arr)
print("The sorted array is:", selection_sort(arr))