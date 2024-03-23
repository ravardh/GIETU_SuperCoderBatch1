def fractional_knapsack(W, N, PW, PP):
    items = [(PP[i] / PW[i], PW[i], PP[i]) for i in range(N)]
    items.sort(reverse=True)

    max_profit = 0
    remaining_weight = W
    for ratio, weight, profit in items:
        if W >= weight:
            max_profit += profit
            W -= weight
        else:
            max_profit += ratio * W
            break
    
    return max_profit
W = 15
N = 4
PW = [5, 10, 10, 5]
PP = [10, 5, 5, 10]

print("Max Profit:", fractional_knapsack(W, N, PW, PP))