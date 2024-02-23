arr = [6,4,2,6,3,8,5,7,4,7,3,8,9,8,2,4,6,10,6,2,3,4,5,1,4,2]
l=0
r=3
sumM = 0
while(r<len(arr)):
    sumM= max(sumM,sum(arr[l:r]))
    l=l+1
    r=r+1
print(sumM)