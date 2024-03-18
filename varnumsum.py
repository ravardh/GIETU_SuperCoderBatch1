l = [5,4,2,6,3,8,9,7,4,7,3,6,9,8,2,4,6,8,6,2,3,4,5,1,4,2]
print(l)
var = int(input('Enter the number of consecutive number sum you want'))
n = len(l)
#i = 0
if var <= n:
    varnumsum = sum(l[:var])
    il = l[:var]
    for i in range(1,n):
        if i+var <= n:
            sum1 = sum(l[i:i+var])
        else:
            break
        if sum1 > varnumsum:
            varnumsum = sum1
            il.append(l[i:i+var])
    print(varnumsum, il[-1])
else:
    print("please enter a valid number of consecutives")
'''
def find_highest_sum(nums, n):
    """
    Finds the highest sum of n consecutive numbers in a list using a single loop.

    Args:
        nums: A list of numbers.
        n: The number of consecutive elements to consider for the sum.

    Returns:
        The highest sum of n consecutive numbers in the list.

    Raises:
        ValueError: If n is greater than the length of the list or non-positive.
    """

    if n <= 0:
        raise ValueError("n must be a positive integer.")

    if n > len(nums):
        raise ValueError("n cannot be greater than the length of the list.")

    current_sum = max_sum = sum(nums[:n])  # Initialize with the sum of the first n elements

    for i in range(n, len(nums)):
        # Calculate the new current_sum by adding the next element and subtracting the (n-1)th element from the previous sum
        current_sum = (current_sum + nums[i]) - nums[i - n]
        max_sum = max(max_sum, current_sum)  # Update max_sum if the current sum is larger

    return max_sum

# Example usage
nums = [1, 2, 3, 4, 5, -10, 2, 3, 4]
n = 4

try:
    highest_sum = find_highest_sum(nums, n)
    print(f"The highest sum of {n} consecutive numbers is: {highest_sum}")
except ValueError as e:
    print(e)
'''
