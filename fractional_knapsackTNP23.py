def fractional_knapsack(W, weights, profits):
    # Indexes of sorted items by their value-to-weight ratio
    indexes = list(range(len(weights)))
    ratios = [p/w for p, w in zip(profits, weights)]
    indexes.sort(key=lambda i: ratios[i], reverse=True)

    max_profit = 0
    for i in indexes:
        if weights[i] <= W:
            max_profit += profits[i]
            W -= weights[i]
        else:
            max_profit += profits[i] * (W / weights[i])
            break

    return max_profit

# Inputs
W = 15  # The total weight (limited) of the products to carry
N = 4   # Total no. of products to choose from
PW = [5, 10, 10, 5]  # Weight of each product
PP = [10, 5, 5, 10]  # Profit from each product

# Calculate maximum profit
max_profit = fractional_knapsack(W, PW, PP)
print(f"Max Profit: {max_profit}")
