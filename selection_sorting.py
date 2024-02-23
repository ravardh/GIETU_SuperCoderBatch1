n=int(input("Enter the number:"))
list_2=[]
for i in range(n):
    m=int(input())
    list_2.append(m)
print(list_2)

def selectionSort(array, n):
    
    for ind in range(n):
        min_index = ind
 
        for j in range(ind + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])

selectionSort(list_2, n)
print('Sorted Array=',list_2)
