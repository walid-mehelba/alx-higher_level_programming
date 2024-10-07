#!/usr/bin/python3
import sys

"""
nqueens.py

This module solves the N-Queens problem using backtracking. The goal is to place
N queens on an N×N chessboard such that no two queens threaten each other.

Usage:
    ./nqueens N

Where:
    - N is an integer representing the size of the chessboard (N×N) and
      the number of queens to be placed.
    - The program prints each possible solution, where each queen is represented
      by a pair [row, column] indicating the position of a queen on the board.

Error Handling:
    - If the wrong number of arguments is provided, it prints:
      "Usage: nqueens N" and exits with status 1.
    - If N is not an integer, it prints: "N must be a number" and exits with
      status 1.
    - If N is less than 4, it prints: "N must be at least 4" and exits with
      status 1.
"""


def is_safe(board, row, col, N):
    """
    Checks if a queen can be placed at board[row][col] without being attacked by any other queen.

    Args:
        board (list): List representing the current chessboard configuration.
                      board[i] holds the column position of the queen in row i.
        row (int): The row where the queen is to be placed.
        col (int): The column where the queen is to be placed.
        N (int): The size of the chessboard (N×N).

    Returns:
        bool: True if placing the queen at board[row][col] is safe, False otherwise.

    This function checks the current board state and verifies that placing a queen
    in the given row and column does not cause conflicts with other queens. It
    checks for column conflicts and diagonal conflicts.
    """
    # Check column conflict
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonal conflicts (upper-left and upper-right diagonals)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(N):
    """
    Solves the N-Queens problem using backtracking.

    Args:
        N (int): The size of the chessboard (N×N) and the number of queens to place.

    Returns:
        list: A list of all possible solutions. Each solution is represented as
              a list of [row, column] pairs where each pair indicates the position
              of a queen on the board.

    This function uses backtracking to generate all valid configurations for placing
    N queens on the chessboard such that no two queens threaten each other.
    """
    def solve(row):
        """
        A recursive helper function to solve the N-Queens problem row by row.

        Args:
            row (int): The current row to place a queen.

        This function tries to place a queen in each column of the current row,
        checks if the position is safe, and then recursively attempts to solve
        the next row. If a solution is found, it is added to the list of solutions.
        """
        if row == N:
            # If all queens are placed, add the solution to the list
            solution = []
            for i in range(N):
                solution.append([i, board[i]])
            solutions.append(solution)
            return

        # Try placing a queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col  # Place queen
                solve(row + 1)    # Move to the next row
                board[row] = -1   # Backtrack

    solutions = []
    board = [-1] * N  # Initialize the board with -1 (no queens placed)
    solve(0)  # Start solving from the first row
    return solutions


def main():
    """
    The main entry point of the program.

    This function handles argument parsing, input validation, and initiates
    the solving process. It checks if the user provided the correct number
    of arguments, verifies that N is a valid integer, and ensures that N is
    greater than or equal to 4.

    If valid, it calls the `solve_nqueens` function to solve the N-Queens
    problem and prints each solution. Each solution is printed as a list of
    [row, column] pairs representing the positions of the queens on the board.
    """
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

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
