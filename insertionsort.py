#In insertion sort, the two adjecent values are checked to find the sortest value
l = [4,7,8,1,9,2,3,6,5]

def insertionSort(l):
    n = len(l)
    for i in range(n):
        minpos = i
        while minpos > 0 and l[minpos]<l[minpos-1]:
            l[minpos],l[minpos-1] = l[minpos-1],l[minpos]
            minpos -= 1
    return l

print(insertionSort(l))
