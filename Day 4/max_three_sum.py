arr=list(map(int, input().split()))
k=int(input())
n=len(arr)
ans=sum(arr[0:k])

for i in range(n-k-1):
  ans=max(ans, sum(arr[i:i+k]))
print(ans)


# Prefix Sum / Sliding Window / Kadane
s=sum(arr[0:k])
ans=s
for i in range(k, n):
  s=(s+arr[i])-arr[i-k]
  ans=max(ans, s)
print(ans)


# Sir's Solution
window=0
s=0
for i in range(k):
  s += arr[i]
window=s

# for i in range(0)