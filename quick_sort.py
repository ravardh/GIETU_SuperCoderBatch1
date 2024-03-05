def quick_sort(li,low,high):
    if low<high:
        index=partion(li,low,high)
        quick_sort(li,low,index-1)
        quick_sort(li,index+1,high)
    


def partion(li,start,end):
    pi=li[end]
    j=start-1
    for i in range(start,end):
        if(li[i]<pi):
            j=j+1
            li[j],li[i]=li[i],li[j]
    j=j+1
    li[end],li[j]=li[j],li[end]

    return j

li=[7,8,2,5,6]
quick_sort(li,0,len(li)-1)
print(li)