def max_sum_of_triplets(arr, num_terms_to_sum):
    max_sum = float('-inf')  # Initialize max_sum with negative infinity
    max_triplet = None  # Initialize variable to store the triplet with max sum
    
    # Iterate through the array until there are enough elements remaining to form a triplet
    for i in range(len(arr) - num_terms_to_sum + 1):
        # Calculate the sum of the current set of terms
        terms_sum = sum(arr[i:i+num_terms_to_sum])
        # Check if the current set's sum is greater than the current maximum sum
        if terms_sum > max_sum:
            max_sum = terms_sum
            max_triplet = tuple(arr[i:i+num_terms_to_sum])  # Update the max triplet
    
    return max_sum, max_triplet

# Take user input for the number of terms in the array
num_terms_total = int(input("Enter the total number of terms in the array: "))
array = []

# Take user input for each term
for i in range(num_terms_total):
    term = int(input(f"Enter term {i + 1}: "))
    array.append(term)

# Take user input for the number of terms to consider for calculating the sum
num_terms_to_sum = int(input("Enter the number of terms to consider for sum: "))

# Calculate maximum sum and the corresponding set of terms
max_sum, max_terms = max_sum_of_triplets(array, num_terms_to_sum)

print("Maximum sum of terms:", max_sum)
print("Terms with maximum sum:", max_terms)