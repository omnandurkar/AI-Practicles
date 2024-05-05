# Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and
# Backtracking for n-queens problem or a graph coloring problem.

N = int(input("Enter number of queens: "))

def print_sol(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_NQ_util(board, col):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_NQ_util(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solve_problem():
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_NQ_util(board, 0):
        print("Solution does not exist")
        return False
    print("Solution for the N Queen problem is:")
    print_sol(board)
    return True

solve_problem()
