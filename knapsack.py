def knapSack(W, wt, val, n):
  K = [[0 for x in range(W + 1)] for x in range(n + 1)]
  selected_items = []
  selected_weights = []

  for i in range(n + 1):
    for w in range(W + 1):
      if i == 0 or w == 0:
        K[i][w] = 0
      elif wt[i-1] <= w:
        K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
        if K[i][w] == val[i-1] + K[i-1][w-wt[i-1]]:
          selected_items.append(i-1)
          print
          selected_weights.append(wt[i-1])
      else:
        K[i][w] = K[i-1][w]

  return K[n][W], selected_items, selected_weights


prices = [10, 5, 15, 7, 6, 18, 3]
wts = [2, 3, 5, 7, 1, 4, 1]
capacity = 15
n = len(prices)

max_value, selected_items, selected_weights = knapSack(capacity, wts, prices, n)
selected_items=set(selected_items)
selected_weights=set(selected_weights)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
print("Selected weights:", selected_weights)