#!/usr/bin/python3

import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n, result):
    if col == n:
        queens_pos = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    queens_pos.append([i, j])
        result.append(queens_pos)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, n, result) or res
            board[i][col] = 0

    return res

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    result = []
    if not solve_n_queens_util(board, 0, n, result):
        return False
    for solution in result:
        for row, col in solution:
            print("[{}, {}]".format(row, col), end=" ")
        print()
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(N)
