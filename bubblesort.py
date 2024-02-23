print("Enter the list (including '[ ]') \n")
l1=eval(input())
print(l1)


for i in range(len(l1)-1):
    for j in range(len(l1)-i-1):
        if l1[j]>l1[j+1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]
print(l1)