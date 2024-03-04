def find(a,s,e):
    i=s
    j=s-1
    pivot=a[e]
    for i in range(s,e):
        if(a[i]<pivot):
            j=j+1
            a[i],a[j]=a[j],a[i]
    j=j+1
    a[j],a[e]=a[e],a[j]
    return j
    
def quicksort(a,s,e):
    if(s<e):
        pivot=find(a,s,e)
        quicksort(a,s,pivot-1)
        quicksort(a,pivot+1,e)
        

if __name__=="__main__":
    arr=[4,8,2,3,7,5,1,9,6]
    quicksort(arr,0,len(arr)-1)
    print(arr)
