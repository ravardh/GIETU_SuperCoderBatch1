def partition(l,st,end):
    pivot = l[end] #let the last element as pivot
    i = st-1 # initially i is -1

    for j in range(st,end):
        if l[j] <= pivot: #compare the j value with pivot element
            i += 1 #increase the i value
            l[i],l[j] = l[j],l[i] #exchange the current value the smaller value less than pivot
    i += 1
    l[i],l[end] = l[end],l[i]
    return i

def quicksorted(l,s,e):
    if s < e:
        r = partition(l,s,e)
        quicksorted(l,s,r-1)
        quicksorted(l,r+1,e)

l = [4,8,2,3,7,5,1,9,6]
quicksorted(l,0,len(l)-1)
print(l)
