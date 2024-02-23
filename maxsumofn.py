b=[5,4,2,6,3,8,9,7,4,7,3,6,9,8,2,4,6,8,6,2,3,4,5,1,4,2]
n=len(b)
c=[]
x=int(input("Enter the no."))
for i in range(n-(x-1)):
    sum=0
    for j in range(i,i+x):
        sum=sum+b[j]
    print(sum)
    c.append(sum)
print(c)
print(max(c))
        