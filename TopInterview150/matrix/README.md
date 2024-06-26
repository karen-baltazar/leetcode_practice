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

## 54. Spiral Matrix

**Description**:
Given an `m x n` matrix, return all elements of the matrix in spiral order.

**Example**:
```plaintext
Input: matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

**Solution**:
To traverse the matrix in spiral order, we maintain boundaries for the top, bottom, left, and right. We iterate through the matrix and adjust these boundaries after processing each row or column. This ensures we cover all elements in the required order.

[Link to code](054_spiral_matrix.py)

**Notes**:
- Time complexity: O(m * n), where m is the number of rows and n is the number of columns.
- Space complexity: O(1) for extra space used (excluding the output list).

## 48. Rotate Image

**Description**:
You are given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. Do not allocate another 2D matrix and do the rotation.

**Example**:
```plaintext
Input: matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Output: [
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
```

**Solution**:
To rotate the image by 90 degrees in-place, we can process the matrix layer by layer, moving elements from the bottom to the top, the left to the bottom, the top to the right, and the saved top to the right. We adjust the boundaries inward after each full layer rotation.

[Link to code](048_rotate_image.py)

**Notes**:
- Time complexity: O(n^2), where n is the dimension of the matrix.
- Space complexity: O(1), since the rotation is done in-place without extra space.