arr=[1,2,3,4,5]
s=[]
nct=int(input("enter the number of consecutive terms"))
for i in range(len(arr)-nct+1):
    s.append((sum(arr[i:i+nct])))
for i in range(len(s)):
    maximum=max(s)
print(maximum)
