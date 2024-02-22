l = [4,7,8,1,9,2,3,6,5]

def selectionSort(l):
    n = len(l)
    for i in range(n):
        minpos = i
        for j in range(i+1,n):
            if l[j] < l[minpos]:
                minpos = j

        l[i],l[minpos] = l[minpos],l[i]
    return l

print(selectionSort(l))
