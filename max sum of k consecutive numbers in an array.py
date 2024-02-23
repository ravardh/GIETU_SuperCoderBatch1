arr=eval(input())
k=int(input())
sum=0
for i in range(k):
    sum=sum+arr[i]
window=sum
for i in range(0,len(arr)-k):
    if window>sum:
        sum=window
    window=window-arr[i]+arr[i+k]
print(sum)
        