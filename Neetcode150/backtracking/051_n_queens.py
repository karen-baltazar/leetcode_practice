from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []  # Stores all possible solutions
        board = [["."] * n for _ in range(n)]  # Initialize the board as a list of lists
        cols = set()  # Tracks used columns
        posDiag = set()  # Tracks used positive diagonals (row + col)
        negDiag = set()  # Tracks used negative diagonals (row - col)

        def backtrack(row: int):
            # If all rows are filled, add the current board configuration to the result
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                # Check if placing a queen here would be valid
                if col in cols or (row + col) in posDiag or (row - col) in negDiag:
                    continue

                # Place the queen on the board
                board[row][col] = 'Q'
                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)

                # Recursively try to place the next queen
                backtrack(row + 1)

                # Backtrack by removing the queen and resetting the state
                board[row][col] = '.'
                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)

        backtrack(0)
        return res
