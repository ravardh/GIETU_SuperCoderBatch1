# DP Approach O(n*W)
def knapSack(C, wt, P, n): 
	dp = [[0 for x in range(C + 1)] for x in range(n + 1)] 
	for i in range(n + 1): 
		for w in range(C + 1): 
			if i == 0 or w == 0: # Base case where no price is there or no capacity is there
				dp[i][w] = 0
			elif wt[i-1] <= w: # if w-wt[i-1] is positive
				dp[i][w] = max(P[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w]) 
			else:
				dp[i][w] = dp[i-1][w] 
	return dp[n][C]

w = list(map(int, input("Enter Item Weight\n").strip().split()))
p = list(map(int, input("Enter Item Price\n").strip().split()))
C = int(input("Knapsack Size: "))
print(knapSack(C, w, p, len(p)))
