def max_sum(arr, consecutive_terms):
    if len(arr) < consecutive_terms:
        return "List should have at least {} elements".format(consecutive_terms)
    
    max_sum = 0 
    
    for i in range(len(arr) - consecutive_terms + 1):
        current_sum = sum(arr[i:i + consecutive_terms])
        if current_sum > max_sum:
            max_sum = current_sum
  
    return max_sum

arr = eval(input("Enter a list: "))
consecutive_terms = int(input("Enter the number of consecutive terms: "))

result = max_sum(arr, consecutive_terms)
print("Maximum sum:", result)