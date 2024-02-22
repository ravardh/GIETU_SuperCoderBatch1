l1=list(map(int, input("Enter values: ").split()))  
temp=0
for i in range(len(l1)):
    min=i
    for j in range(i+1,len(l1)):
        if(l1[min]>l1[j]):
             min=j
    temp=l1[i]
    l1[i]=l1[min]
    l1[min]=temp
    
print(l1)
