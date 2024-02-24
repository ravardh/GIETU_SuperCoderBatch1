def find(a,s,e):
    p=a[e]
    i=s
    j=s-1
    for i in range(s,e):
        if(a[i]<a[j]):
            a[i],a[j]=a[j],a[i]
    a[j],a[e]=a[e],a[j]
    return j

def quicksort(a,s,e):
    if s<e:
        pi=find(a,s,e)
        quicksort(a,s,pi-1)
        quicksort(a,pi+1,e)


if __name__=="__main__":
    a=[4,8,5,3,7,2,9,1]
    quicksort(a,0,len(a)-1)
    print(a)