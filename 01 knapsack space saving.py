def knapsack(wt, val, n, W):
    take = 0
    dp = [[0 for i in range(W + 1)] for j in range(n)]

    for i in range(wt[0], W + 1):
        dp[0][i] = val[0]
        
    for ind in range(1, n):
        for cap in range(W + 1):
            notTaken = dp[ind - 1][cap]
            
            if wt[ind] <= cap:
                take = val[ind] + dp[ind - 1][cap - wt[ind]]
                
            dp[ind][cap] = max(notTaken, take)
    
    
    return dp[n - 1][W]

wt = [2, 3, 5, 7, 1, 4]
val = [10, 5, 15, 7, 6, 18]
W = 15
n = len(wt)

print("The Maximum value of items the thief can steal is", knapsack(wt, val, n, W))

