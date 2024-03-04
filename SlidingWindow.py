# Approach 1
l = [5,4,2,6,3,8,9,7,4,7,3,6,9,8,2,4,6,8,6,2,3,4,5,1,4,2]
lsum = []
for i in range(0,len(l)-2):
    sum = 0
    for j in range(i,i+3):
        sum = sum +  l[j] 
        lsum.append(sum)
print(max(lsum))


# Approach 2 (optimized)
l = [5,4,2,6,3,8,9,7,4,7,3,6,9,8,2,4,6,8,6,2,3,4,5,1,4,2]
lsum = []
win_size = int(input("Enter window size: "))

for i in range(len(l) - win_size + 1):
    print(l[i:i+win_size])
    window_sum = sum(l[i:i+win_size])
    lsum.append(window_sum)

print(max(lsum))