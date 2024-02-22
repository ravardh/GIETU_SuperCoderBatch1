def BubbleSort(arr):
    
  for i in range(len(arr)-1):
 
    for j in range(0, len(arr) - i - 1):
 
      if arr[j] > arr[j + 1]:
 
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp

a =  [22, 18, 48, 32, 12]
BubbleSort(a)
print(a)
