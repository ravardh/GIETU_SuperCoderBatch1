#Sum of three consecutive terms and maximize the sum of 3 terms
array = [5, 4, 2, 6, 3, 8, 9, 7, 4, 7, 3, 6, 9, 8, 2, 4, 6, 8, 6, 2, 3, 4, 5, 1, 4, 2]

# Calculate the sum of 3 consecutive terms and store them in a list
sum = [sum( array[i:i+3]) for i in range(len(array)-2)]

# Find the maximum value in the list of sums
sum_maximize = max(sum)

print("Maximum sum of 3 consecutive terms:", sum_maximize)



#2-Sum of three consecutive terms and maximize the sum of 3 terms as user input

arr_str = input("Enter the elements of the array ")
arr_str_list = arr_str.split()
arr = []

for element in arr_str_list:
    arr.append(int(element))

sum_of_3 = []

for i in range(len(arr)-2):
    current_sum = sum(arr[i:i+3])
    sum_of_3.append(current_sum)

max_sum_of_3 = max(sum_of_3)

print("Maximum sum of 3 consecutive terms:", max_sum_of_3
      

#3-sliding window
arr = [1, 3, 5, 2, 7, 4, 8, 9, 5, 3, 5, 7, 9, 3, 2, 0]
k = int(input("enter the value of window: "))
sum = 0
max = 0
for i in range(k):
    sum = sum+arr[i]
max = sum
for i in range(k, len(arr)):
    sum = sum-arr[i-k]+arr[i]
    if (sum > max):
        max = sum
print(max)