
lst=[int(x) for x in input("Enter the list sep by commas:\n").split(",")]
for i in range(1, len(lst)):
        key=lst[i]
        j=i-1 
        while j>=0 and key<lst[j]:
            lst[j+1]=lst[j]
            j-= 1
        lst[j+1] = key
print(lst)
