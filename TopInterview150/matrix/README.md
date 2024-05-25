# Problems

## 36. Valid Sudoku

**Description**:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

**Example**:
```plaintext
Input: 
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
```

**Solution**:
To validate the Sudoku board, we need to check three conditions:
1. Each row must contain unique digits (excluding '.').
2. Each column must contain unique digits (excluding '.').
3. Each 3x3 sub-box must contain unique digits (excluding '.').

We use sets to track the digits we have seen so far for each row, column, and sub-box. If a duplicate is found, we return false.

[Link to code](036_valid_sudoku.py)

**Notes**:
- Time complexity: O(n^2), where n is the length of the board (9 in this case).
- Space complexity: O(n), due to the use of sets to track seen digits.
