def merge(L,R):
    idx=0
    i=0
    j=0
    temp=[0]*(len(L)+len(R))
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            temp[idx]=L[i]
            i=i+1
        else:
            temp[idx]=R[j]
            j=j+1
        idx=idx+1
    while i<len(L):
        temp[idx]=L[i]
        idx=idx+1
        i=i+1
    while j<len(R):
        temp[idx]=R[j]
        idx=idx+1
        j=j+1
    
    return temp
    

def merge_sort(arr,l,h):
    if l==h:
        return [arr[l]]
    m = (l+h)//2
    L=merge_sort(arr,l,m)
    R=merge_sort(arr,m+1,h)
    return merge(L,R)

if __name__=="__main__":
    arr=eval(input())
    a=merge_sort(arr,0,len(arr)-1)
    print(a)