class Solution(object):
    def isValidSudoku(self, board):
        # Hint: Think about the starting points and bounds for iterating through sub-boxes.
                
        # Validate rows
        for i in range(9):
            row = set()
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if num in row:
                        return False  # Duplicate found in row
                    row.add(num)

        # Validate columns
        for i in range(9):
            column = set()
            for j in range(9):
                num = board[j][i]
                if num != ".":
                    if num in column:
                        return False  # Duplicate found in column
                    column.add(num)

        # Validate 3x3 sub-boxes
        for i in range(0, 9, 3):  # Iterate over sub-box start row indices
            for j in range(0, 9, 3):  # Iterate over sub-box start column indices
                box = set()
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        num = board[row][col]
                        if num != ".":
                            if num in box:
                                return False  # Duplicate found in 3x3 sub-box
                            box.add(num)

        return True  # All checks passed, the board is valid