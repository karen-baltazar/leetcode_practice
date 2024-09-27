class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the dimensions of the board
        rows, cols = len(board), len(board[0])
        word_len = len(word)
        
        # Handle the case where the board is a single cell
        if rows == 1 and cols == 1:
            return board[0][0] == word

        # Backtracking function to explore possible paths
        def backtrack(position, char_index):
            row, col = position
            
            # If the entire word has been matched, return True
            if char_index == word_len:
                return True

            # If the current cell doesn't match the current character of the word, return False
            if board[row][col] != word[char_index]:
                return False

            # Temporarily mark the current cell as visited
            current_char = board[row][col]
            board[row][col] = '#'

            # Explore all four possible directions (up, down, left, right)
            for row_offset, col_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + row_offset, col + col_offset
                # Check if the new position is within bounds
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if backtrack((new_row, new_col), char_index + 1):
                        return True

            # Restore the cell's original value after exploring all options
            board[row][col] = current_char
            return False

        # Check every cell in the board as the starting point
        for row in range(rows):
            for col in range(cols):
                # If a valid path is found starting from this cell, return True
                if backtrack((row, col), 0):
                    return True

        # If no valid path is found, return False
        return False

