def count_pic(arr):
  n = len(arr)
  curr, ans = arr[0], 1
  for i in range(1, n):
    if arr[i] > curr:
      ans += 1
    curr = max(curr, arr[i])
  return ans

def testcases():
  tc = {
    "1": [10, 15, 20, 10, 12], 
    "2": [8, 8, 8, 8], 
    "3": [5, 10, 5, 15, 5, 20], 
    "4": [25, 15, 30, 20, 25]
  }
  inp = input("Choose Testcase[1/2/3/4]: ")
  print(f"Testcase #{inp}:\nBuilding Heights: {tc[inp]}\nTotal Pictues: {count_pic(tc[inp])}")


if __name__ == "__main__":
  testcases()
  # arr = list(map(int, input().strip().split()))
  # print(count_pic(arr))