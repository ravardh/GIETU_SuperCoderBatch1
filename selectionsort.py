l1=eval(input())
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i]<=l1[j]:
            l1[j],l1[i]=l1[i],l1[j]
print(l1)