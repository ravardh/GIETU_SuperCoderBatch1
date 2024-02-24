a = [1,3,5,2,7,4,8,9,5,3,5,7,9,2,0]
sum=0
n=len(a)
for i in range(n):
    while i < n-2:
        if(a[i] + a[i+1] +a[i+2] > sum):
            sum = a[i] +a[i+1] + a[i+2]
        i+=1
print(sum)