l = [4,7,8,1,9,2,3,6,5]

def bubbleSort(l):
    n=len(l)
    for i in range(n):
       for j in range(n-i-1):
           if l[j]>l[j+1]:
              l[j],l[j+1]=l[j+1],l[j]
    return l
print(bubbleSort(l))