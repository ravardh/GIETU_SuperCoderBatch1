def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Check upper diagonal on right side
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

def solve_n_queens_util(board, row, N):
    if row == N:
        return True
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, N):
                return True
            board[row][col] = 0
    
    return False

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens_util(board, 0, N):
        print("Solution does not exist")
        return False
    
    print("One possible solution:")
    for row in board:
        print(" ".join(map(str, row)))

    return True

# Example usage
N = 8
solve_n_queens(N)