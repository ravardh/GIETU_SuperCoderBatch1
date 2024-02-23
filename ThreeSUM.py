print("Array bharo :")
arr=eval(input())
idx=int(input("Kitna sum chahiye aapko : "))
s=sum(arr[:idx])
prev=s
for i in range(idx,len(arr)):
    s=s+arr[i]-arr[i-idx]
    if prev<s:
        prev=s
print(prev)