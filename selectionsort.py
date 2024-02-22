l = [4,7,8,1,9,2,3,6,5]

def selectionSort(l):
    n=len(l)
    for i in range(n):
        pos=i
        for j in range(i+1,n):
            if l[j]<l[pos]:
                pos=j
        l[i],l[pos] = l[pos],l[i]
    return l
print(selectionSort(l))
                
             
    
    