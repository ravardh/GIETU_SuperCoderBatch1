def N_Queen(n):
  col = set()
  posDiag = set() # r + c
  negDiag = set() # r - c
  res = []
  board = [["#"] * n for i in range(n)]
  flag = False
  def backtrack(r):
    nonlocal flag
    if flag:
      return
    if r == n:  # valid solution
      temp = ["".join(row) for row in board]
      res.append(temp)
      flag = True
      return
    
    for c in range(n):
      if c in col or (r+c) in posDiag or (r-c) in negDiag:
        continue  # unsafe
      
      col.add(c)
      posDiag.add(r+c)
      negDiag.add(r-c)
      board[r][c] = "Q"

      backtrack(r+1)

      col.remove(c)
      posDiag.remove(r+c)
      negDiag.remove(r-c)
      board[r][c] = "#"
  backtrack(0)
  return res

n = int(input("N: "))
possibilities = N_Queen(n)
for i in range(len(possibilities)):
  print(f"Instance {i+1}")
  for j in possibilities[i]:
    print(*j)
  print("~"*(n*2))