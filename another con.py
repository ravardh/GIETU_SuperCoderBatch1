arr=eval(input())
k=int(input())
max1=0
for i in range(0,len(arr)-k+1):
    sum=0
    for j in range(k):
      sum=sum+arr[j+i]
    max1=max(max1,sum)
print(max1)