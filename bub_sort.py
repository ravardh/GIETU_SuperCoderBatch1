lst=[int(x) for x in input("Enter the elements of the list separated by commas:\n").split(",")]
i=0
for i in range(len(lst)-i):
    for j in range(i,len(lst)-i-1):
        if(lst[j]>lst[j+1]):
            lst[j+1],lst[j]=lst[j],lst[j+1]
print(lst)
