arr=[int(x) for x in input("Enter the array elements:\n").split(",")]
maxm=min(arr)-1
ctr=0
for ele in arr:
    if ele>maxm and arr.count(ele)>1:
        maxm=ele
        arr=[x for x in arr if ele!=x]
        ctr+=1
    elif ele>maxm:
        
        ctr+=1
        maxm=ele
print(ctr)