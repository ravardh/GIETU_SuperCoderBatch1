def knapSack(capacity, weights, values, n):
   #initialization of the table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Filing the initialization table using bottom up approach
    for i in range(1, n + 1):
        for w in range(1, capacity + 1): #nested loop ittreates form 1 to capapcity,used  for itreate over each possible knapsack capacity.
            if weights[i - 1] <= w: #it checks if the current weight is less than or equal to the current knapsack capacity
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]) #If the weight of the current item is less than or equal to the current knapsack capacity, then this line calculates the maximum value that can be obtained with the current item and the current knapsack capacity. It does this by taking the maximum of two values: the maximum value that can be obtained without including the current item (dp[i - 1][w]), and the maximum value that can be obtained by including the current item (dp[i - 1][w - weights[i - 1]] + values[i - 1]).
            else: #If the weight of the current item is greater than the current knapsack capacity, then this block of code is executed.
                dp[i][w] = dp[i - 1][w] #If the weight of the current item is greater than the current knapsack capacity, then the maximum value that can be obtained with the current item and the current knapsack capacity is the same as the maximum value that can be obtained without the current item

    return dp[n][capacity] # After the memoization table has been filled, this line returns the maximum value that can be obtained with the given capacity and items. This value is stored in the last cell of the memoization table 

#system input given by me
values = [10, 5, 15, 7, 6, 18, 3]
weights = [2, 3, 5, 7, 1, 4, 1]
capacity = 15
n = len(values)

print(knapSack(capacity, weights, values, n))  