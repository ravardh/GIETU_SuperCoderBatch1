l = [5,4,2,6,3,8,9,7,4,7,3,6,9,8,2,4,6,8,6,2,3,4,5,1,4,2]
i,j,k = 0,1,2
n = len(l)
threenumsum = 0

while k < n :
    sum1 = l[i]+l[j]+l[k]
    
    if threenumsum < sum1:
        threenumsum = sum1
        bigi = i
        bigj = j
        bigk = k
    i += 1
    j += 1
    k += 1

print(l[bigi],l[bigj],l[bigk],threenumsum)
