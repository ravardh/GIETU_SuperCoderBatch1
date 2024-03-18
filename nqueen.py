
def is_safe(board, row, col, n):
   
    for i in range(row):
        if board[i][col] == 1:
            return False

  
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

   
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, n):
    if row == n:
       
        for i in range(n):
            print("".join(str(board[i][j]) for j in range(n)))
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n)
            board[row][col] = 0

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solve_n_queens_util(board, 0, n)


n = 4
solve_n_queens(n)

