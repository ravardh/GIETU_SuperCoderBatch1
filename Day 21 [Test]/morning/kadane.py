def count_pic(arr):
  n = len(arr)
  curr, ans = arr[0], 1
  for i in range(1, n):
    if arr[i] > curr:
      ans += 1
    curr = max(curr, arr[i])
  return ans

def testcases():
  arr = [[10, 15, 20, 10, 12], [8, 8, 8, 8], [5, 10, 5, 15, 5, 20], [25, 15, 30, 20, 25]]
  for i in arr:
    print(f"{i}: {count_pic(i)}")

if __name__ == "__main__":
  # testcases()
  arr = list(map(int, input().strip().split()))
  print(count_pic(arr))