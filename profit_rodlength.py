def max_profit(length, price):
    n = len(length)
    # Create a list to store the maximum profit for each rod length
    max_profit = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            max_profit[i] = max(max_profit[i], price[j] + max_profit[i - j - 1])

    return max_profit[n]

# Test cases
length1 = [1, 2, 3, 4, 5, 6, 7, 8]
price1 = [1, 5, 8, 9, 10, 17, 17, 20]
print("Max profit:", max_profit(length1, price1))

length2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
price2 = [3, 5, 8, 9, 10, 17, 17, 20, 22, 25, 30, 35]
print("Max profit:", max_profit(length2, price2))
