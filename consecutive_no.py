'''arr=[5,4,2,6,3,8,9,7,4,7,3,6,9,8,2,4,6,8,6,2,3,4,5,1,4,2]
m=0
l=[]
for i in range(0,len(arr)):
    m=0
    for j in range(i,i+3):
        if(j==len(arr)):
           break
        m=m+arr[j]
    l.append(m)
print(max(l))
        
x=eval(input("eneter elements into list"))
y=list(x)
l1=[]
for i in range(0,len(x)):
    m=0
    for j in range(i,i+3):
        if(j==len(arr)):
           break
        m=m+arr[j]
    l1.append(m)
print(max(l1))
'''
p=[]
for i in input("enter elements").split():
    p.append(int(i))
print(p)
f=[]
abc=int(input("enter no.of consecutive elements"))
for i in range(0,len(p)):
    m=0
    for j in range(i,i+abc):
        if(j==len(p)):
           break
        m=m+p[j]
    f.append(m)
print(max(f))
          
