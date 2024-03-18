def knapsack(wt, val, capa):
    n = len(wt)
    
    M = [[0] * (capa + 1) for _ in range(n + 1)]

    
    for i in range(1, n + 1):
        for w in range(1, capa + 1):
           
            if wt[i - 1] > w:
                M[i][w] = M[i - 1][w]
           
            else:
                M[i][w] = max(M[i - 1][w], val[i - 1] + M[i - 1][w - wt[i - 1]])

    
    selected_items = []
    i = n
    j = capa
    while i > 0 and j > 0:
        if M[i][j] != M[i - 1][j]:
            selected_items.append(i - 1)
            j -= wt[i - 1]
        i -= 1
    
    return M[n][capa], selected_items

wt = [2,3,5,7,1,4,1]
val = [10,5,15,7,6,18,3]
capa = 15
max_value, selected_items = knapsack(wt, val, capa)
print("Maximum value:", max_value)
print("Selected items:", selected_items)

