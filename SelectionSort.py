def selectionSort(array, size):
    
    for l in range(size):
        min_index = l
 
        for j in range(l + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[l], array[min_index]) = (array[min_index], array[l]) 



arr = [-1,-45,2,4,3,7]
size = len(arr)
selectionSort(arr,size)
print('The sorted array is:')
print(arr)