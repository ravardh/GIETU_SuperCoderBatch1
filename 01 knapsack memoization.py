def knapsackMain(wt, val, ind, W, dp):
    take = 0
    
    if ind == 0:
        if wt[0] <= W:
            return val[0]
        else:
            return 0
    
    if dp[ind][W] != -1:
        return dp[ind][W]
    
    notTake = 0 + knapsackMain(wt, val, ind-1, W, dp)

    if wt[ind] <= W:
        take = val[ind] + knapsackMain(wt, val, ind - 1, W - wt[ind], dp)
    
    dp[ind][W] = max(notTake, take)
    return dp[ind][W]

def knapsack(wt, val, n, W):
    dp = [[-1 for j in range(W + 1)] for i in range(n)]
    return knapsackMain(wt, val, n - 1, W, dp)

wt = [2, 3, 5, 7, 1, 4]
val = [10, 5, 15, 7, 6, 18]
W = 15
n = len(wt)

print("The Maximum value of items the thief can steal is", knapsack(wt, val, n, W))

