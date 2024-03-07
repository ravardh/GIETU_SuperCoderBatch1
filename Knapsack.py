def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    max_value = dp[n][capacity]

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()
    return max_value, selected_items

weights = [2, 3, 5, 7, 1, 4, 1]
values = [10, 5, 15, 7, 6, 18, 3]
capacity = 15

max_value, selected_items = knapsack(weights, values, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
