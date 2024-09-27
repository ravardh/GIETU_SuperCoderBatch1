def mergeSort(l):
    if len(l) > 1:        
        r = len(l)//2 #  r is the point where the array is divided into two subarrays
        L = l[:r]
        M = l[r:]
        
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                l[k] = L[i]
                i += 1
            else:
                l[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            l[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            l[k] = M[j]
            j += 1
            k += 1

    return l

l = [4,8,2,3,7,5,1,9,6]
print("Sorted list using Merge Sort is: ",mergeSort(l))
