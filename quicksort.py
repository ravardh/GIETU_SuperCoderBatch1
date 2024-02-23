def find(arr,S,E):
    P=arr[E]
    j=S-1
    for i in range(S,E):
        if arr[i]<P:
            j=j+1
            arr[i],arr[j]=arr[j],arr[i]
    j=j+1
    arr[j],arr[E] = arr[E],arr[j]
    return j


def quicksort(arr,S,E):
    if S<E:
        pi=find(arr,S,E)
        quicksort(arr,S,pi-1)
        quicksort(arr,pi+1,E)

if __name__=='__main__':
    arr= eval(input(("Pass the array with '[ ]'")))
    quicksort(arr,0,len(arr)-1)
    print("Sorted array is: ",arr)