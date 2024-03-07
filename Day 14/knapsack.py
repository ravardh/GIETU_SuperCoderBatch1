def knapsack(wt, val, W, n):
	t = [[-1 for i in range(W + 1)] for j in range(n + 1)] 
	
	# base conditions 
	if n == 0 or W == 0: 
		return 0
	if t[n][W] != -1: 
		return t[n][W] 

	if wt[n-1] <= W: 
		t[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1)) 
		return t[n][W] 
	elif wt[n-1] > W: 
		t[n][W] = knapsack(wt, val, W, n-1) 
		return t[n][W] 

w = list(map(int, input("Enter Item Weight\n").strip().split()))
p = list(map(int, input("Enter Item Price\n").strip().split()))
W = int(input("Knapsack Size: "))
print(knapsack(w, p, W, len(p)))
