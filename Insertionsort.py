l = [4,7,8,1,9,2,3,6,5]

def insertionSort(l):
    n=len(l)
    for i in range(n):
       pos=i
       while pos>0 and l[pos]<l[pos-1]:
           l[pos],l[pos-1] = l[pos-1],l[pos]
           pos-=1
    return l
print(insertionSort(l))