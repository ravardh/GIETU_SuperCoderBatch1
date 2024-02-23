list = [4,7,8,1,9,2,3,6,5]

def insertionSort(list):
    n = len(list)
    for i in range(n):
        j = i
        while j > 0 and list[j-1]>list[j]:
            temp = list[j-1]
            list[j-1] = list[j]
            list[j] = temp
            j -= 1
    return list

print(insertionSort(list))
