arr = [5, 4, 2, 6, 3, 8, 9, 7, 4, 7, 3, 6, 9, 8, 2, 4, 6, 8, 6, 2, 3, 4, 5, 1, 4, 2]

# Calculate the sum of 3 consecutive terms and store them in a list
sum_of_3 = [sum(arr[i:i+3]) for i in range(len(arr)-2)]

# Find the maximum value in the list of sums
max_sum_of_3 = max(sum_of_3)

print("Maximum sum of 3 consecutive terms:", max_sum_of_3)
