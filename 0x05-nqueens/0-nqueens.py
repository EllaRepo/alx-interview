#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at position (row, col)
       on the board.
    Args:
        board: matrix
        row: row
        col: column
        N: board size
    """
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """Solve the N queens problem and print every possible solution to
       the problem.
    Args:
        N: integer number
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def solve(board, row):
        """
        Recursively solve the N queens problem using backtracking.
        """
        if row == N:
            print([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve(board, row + 1)

    solve([0] * N, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solve_nqueens(sys.argv[1])
