list = [4,7,8,1,9,2,3,6,5]

def bubbleSort(list):
    n = len(list)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                temp = list[j];
                list[j] = list[j+1];
                list[j+1] = temp;
    return list


print(bubbleSort(list))