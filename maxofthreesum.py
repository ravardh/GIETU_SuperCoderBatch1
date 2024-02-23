a=[5,4,2,6,3,8,9,7,4,7,3,6,9,8,2,4,6,8,6,2,3,4,5,1,4,2]
n=len(a)
b=[]
sum=0
for i in range(n-2):
    sum=a[i]+a[i+1]+a[i+2]
    print(sum)
    b.append(sum)
    sum=0
print(b)
print(max(b))

