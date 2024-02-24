list=eval(input())
k=int(input())
sum=0
for i in range(k):
    sum=sum+list[i]
window=sum
for i in range(0,len(list)-k):
    if window>sum:
        sum=window
    window=window-list[i]+list[i+k]
print(sum)
        