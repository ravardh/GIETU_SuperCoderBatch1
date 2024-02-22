#Selection Sort:
def SelectionSort(array,size):
    for ind in range(size):
        min_index = ind
        for j in range(ind+1,size):
            if array[j]< array[min_index]:
                min_index = j
        (array[ind],array[min_index]) = (array[min_index],array[ind])
arr = [4,6,8,13,17,9,10]
size = len(arr)
SelectionSort(arr,size)
print("the sorted array is:")
print(arr)
