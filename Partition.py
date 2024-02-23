def partition(l,st,end):
    pivot = l[end] #let the last element as pivot
    i = st-1

    for j in range(st,end):
        if l[j] <= pivot:
            i += 1
            l[i],l[j] = l[j],l[i]
    i += 1
    l[i],l[end] = l[end],l[i]
    return i

def sorted(l,s,e):
    if s < e:
        r = partition(l,s,e)
        sorted(l,s,r-1)
        sorted(l,r+1,e)

l = [4,8,2,3,7,5,1,9,6]
sorted(l,0,len(l)-1)
print(l)