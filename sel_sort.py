lst=[int(x) for x in input("Enter the elements of the list separated by commas:\n").split(",")]
for i in range(len(lst)-1):
    x=i
    for j in range(i,len(lst)):
        if(lst[j]<lst[x]):
            x=j
    if(x!=i):
        lst[i],lst[x]=lst[x],lst[i] 
print(lst)

