def find_max_profit(l, p):
  n = len(l)
  dp = [0] * (max(l)+1)
  for i, j in zip(l, p):
    # initialize the dp
    dp[i] = j
  # print(*dp)
  for i in l:
    for j in range(i):
      dp[i] = max(dp[i], dp[j]+dp[i-j])
  # print(*dp)
  return dp[n]

def testcases():
  tc = {
    "1": {
      "length": [1, 2, 3, 4, 5, 6, 7, 8], 
      "price": [1, 5, 8, 9, 10, 17, 17, 20]
    },
    "2": {
      "length": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
      "price": [3, 5, 8, 9, 10, 17, 17, 20, 22, 25, 30, 35]
    }
  }
  inp = input("Choose Testcase[1/2]: ")
  print(f"Testcase #{inp}:\nLength: {tc[inp]['length']}\nPrice: {tc[inp]['price']}")
  print(find_max_profit(tc[inp]["length"], tc[inp]["price"]))

if __name__ == "__main__":
  testcases()
  # l = list(map(int, input().strip().split()))
  # p = list(map(int, input().strip().split()))
  # print(find_max_profit(l, p))
