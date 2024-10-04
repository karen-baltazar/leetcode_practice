class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Hint: Use DFS to traverse and mark 'O's connected to the border.

        rows, cols = len(board), len(board[0])

        def capture(r, c):
            # Base case: if out of bounds or not 'O', return
            if (r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O"):
                return

            # Mark the cell as temporary 'T' to avoid revisiting
            board[r][c] = "T"
            # Recursively capture all connected 'O's
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Step 1: Capture unsurrounded regions (O -> T) using DFS
        for r in range(rows):
            for c in range(cols):
                # Start DFS from 'O's on the border
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    capture(r, c)

        # Step 2: Capture surrounded regions (O -> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Step 3: Uncapture unsurrounded regions (T -> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
