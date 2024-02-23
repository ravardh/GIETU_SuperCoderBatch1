arr = [5,4,2,6,3,8,9,7,4,7,3,6,9,8,2,4,6,8,6,2,3,4,5,1,4,2]
l=0
r=3
sumM = 0
while(r<len(arr)):
    sumM= max(sumM,sum(arr[l:r]))
    l=l+1
    r=r+1
print(sumM)

def max_sum(arr):
    if len(arr) < 3:
        return "List should have at least 3 elements"
    
    max_sum = 0 
    
    for i in range(len(arr) - 2):
        current_sum = arr[i] + arr[i + 1] + arr[i + 2]
        if current_sum > max_sum:
            max_sum = current_sum
  
    return max_sum


arr = eval(input("Enter a list:"))
result = max(arr)
print("Maximum sum:", result)
