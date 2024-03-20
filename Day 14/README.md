Q1) What are the types of programming methodology  
- Brute Force
- Divide and Conquer 
- Greedy Algorithm
- Recursion
- Backtracking
- Dynamic Programming

Q2) difference between tabulation and memoization  
the main difference between tabulation and memoization is that memoization is a top-down approach that uses a lookup table to store the results of function calls, while tabulation is a bottom-up approach that builds up the solution to a problem by solving smaller subproblems and storing the results in a table


## Rat in a maze problem
The rat is initially at position (0,0) and it need to reach bottom right of the grid by taking the minimum cost path.  
> Original array  

|   |   |   |
| - | - | - |
| 1 | 2 | 1 |
| 1 | 3 | 1 |
| 2 | 3 | 1 |

> Tabulation array  
`dp[i][j] = arr[i][j]  + min(dp[i][j-1], dp[i-1][j])`

|   |   |   |
| - | - | - |
| 1 | 3 | 4 |
| 2 | 5 | 5 |
| 4 | 7 | 6 |

`ans = dp[n][m]`

## 0/1 Knapsack Problem [Greedy vs DP]
You have a set of items, each with a weight and a price, and you need to determine the most valuable combination of items that can be packed into a knapsack of limited capacity. The name "0/1" comes from the fact that you can either take an item (1) or leave it (0).  

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
| Item No🏷️ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 
| Price 💸 | 10 | 5 | 15 | 7 | 6 | 18 | 3 | 
| Weight⚓ | 2 | 3 | 5 | 7 | 1 | 4 | 1 | 

Capacity: **15 Kgs**  

Constraints: Maximize the price within the given capacity  


**Greedy Approach**

| Item No🏷️ | Price/Weight |
| :-------- | :----------- |
| 1 | 5 |
| 2 | 1.66 |
| 3 | 3 |
| 4 | 1 |
| 5 | 6 |
| 6 | 4.5 |
| 7 | 3 |

|   |   |   |   |   |   |
| - | - | - | - | - | - |
| Item No🏷️ | 5 | 1 | 6 | 3 | 7 | 
| Weight⚓ | 1 | 2 | 4 | 5 | 1 |
| Space Left🎒 | 14 | 12 | 8 | 3 | 2 |

**Dynamic Programming**
=============================================================

First, let's define two arrays:

* `dp[i][j]`: The maximum value that can be obtained with the first `i` items and a knapsack capacity of `j`.
* `wt[i]`: The weight of the `i`-th item.
* `val[i]`: The value of the `i`-th item.

The base case is:

* `dp[0][j] = 0`, for all `j`, since we can't include any items when `i = 0`.

The recursive case is:

* If the weight of the `i`-th item is greater than the capacity `j`, then we can't include it, so `dp[i][j] = dp[i-1][j]`.
* Otherwise, we have two choices: either include the `i`-th item or don't include it. If we include it, then the maximum value we can get is `val[i] + dp[i-1][j-wt[i]]`. If we don't include it, then the maximum value we can get is `dp[i-1][j]`. Therefore, `dp[i][j] = max(val[i] + dp[i-1][j-wt[i]], dp[i-1][j])`.

The answer is the maximum value that can be obtained with all the items and the given capacity, which is `dp[n][W]`, where `n` is the number of items and `W` is the capacity.
