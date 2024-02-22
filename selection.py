list = [4,7,8,1,9,2,3,6,5]

def selectionSort(list):
    n = len(list)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if list[j] < list[min]:
                min = j

        temp = list[min]
        list[min] = list[i]
        list[i] = temp
    return list

print(selectionSort(list))