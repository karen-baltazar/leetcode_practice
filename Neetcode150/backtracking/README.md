# Problems

| Problem Number | Problem Name                      | Explanation                                           | Code                                            |
|----------------|-----------------------------------|-------------------------------------------------------|-------------------------------------------------|
| 90  | [Subsets II](#90-subsets-ii)     | [Explanation](#90-subsets-ii) | [Python Code](./090_subsets_ii.py) |
| 40  | [Combination Sum II](#40-combination-sum-ii) | [Explanation](#40-combination-sum-ii) | [Python Code](./040_combination_sum_ii.py) |
| 131 | [Palindrome Partitioning](#131-palindrome-partitioning) | [Explanation](#131-palindrome-partitioning)       | [Python Code](./131_palindrome_partitioning.py) |
| 51  | [N-Queens](#51-n-queens) | [Explanation](#51-n-queens) | [Python Code](./051_n_queens.py) |
| 78   | [Subsets](#78-subsets) | [Explanation](#78-subsets) | [Python Code](./078_subsets.py) |
| 46   | [Permutations](#46-permutations)  | [Explanation](#46-permutations) | [Python Code](./046_permutations.py) |
| 39   | [Combination Sum](#39-combination-sum) | [Explanation](#39-combination-sum) | [Python Code](./039_combination_sum.py) |
| 17   | [Letter Combinations of a Phone Number](#17-letter-combinations-of-a-phone-number) | [Explanation](#17-letter-combinations-of-a-phone-number) | [Python Code](./017_letter_combinations.py) |
| 79   | [Word Search](#79-word-search) | [Explanation](#79-word-search) | [Python Code](./079_word_search.py) |

## 90. Subsets II

**Description**:
Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets.

**Example**:
```plaintext
Input: nums = [1, 2, 2]
Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
Explanation: The subsets contain duplicates, so [2] and [2, 2] should only appear once.
```

**Solution**:
The approach uses backtracking to explore all possible subsets:
- Sort the array to handle duplicates easily.
- Use a recursive function to decide whether to include each number.
- Skip over duplicates during the recursive exploration.

[Link to code](./090_subsets_ii.py)

**Notes**:
- Time complexity: O(n * 2^n) due to generating all subsets and creating copies of subsets.
- Space complexity: O(n) for the recursion stack and storing subsets.

## 40. Combination Sum II

**Description**:
Given a collection of candidate numbers (including duplicates) and a target number, find all unique combinations in candidates where the candidate numbers sum to the target. Each number in candidates may only be used once in the combination.

**Example**:
```plaintext
Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
Explanation: Each combination sums to 8 without duplicates.
```

**Solution**:
The approach uses backtracking with a sorted list to handle duplicates:
- Recursively explore adding numbers if it doesn't exceed the target.
- If the target is met, add the combination.
- Skip duplicate numbers to avoid redundant combinations.

[Link to code](./040_combination_sum_ii.py)

**Notes**:
- Time complexity: O(2^n), as each element can be included or excluded in subsets.
- Space complexity: O(n), due to the recursion stack and current combination storage.

## 131. Palindrome Partitioning

**Description**:
Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

**Example**:
```plaintext
Input: s = "aab"
Output: [["a", "a", "b"], ["aa", "b"]]
Explanation: Possible partitions include single letters or "aa" as a palindrome.
```

**Solution**:
The approach uses backtracking to explore all possible partitions:
- If the current substring is a palindrome, add it to the current partition.
- Recursively partition the remaining substring.
- Backtrack to explore other possible partitions.

[Link to code](./131_palindrome_partitioning.py)

**Notes**:
- Time complexity: O(n * 2^n), due to checking palindromes and generating all subsets.
- Space complexity: O(n), for the recursion stack and storing partitions.

## 51. N-Queens

**Description**:  
The N-Queens problem asks you to place N queens on an N x N chessboard such that no two queens threaten each other. A queen can attack horizontally, vertically, and diagonally. Find all distinct solutions to the N-Queens problem.

**Example**:
```plaintext
Input: n = 4
Output: 
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There are two distinct solutions to the 4-Queens puzzle.
```

**Solution**:  
This approach uses backtracking to explore all possible placements of queens:
- The board is initialized as a list of lists (`n x n`), filled with `"."`.
- Three sets track columns (`cols`), positive diagonals (`posDiag`), and negative diagonals (`negDiag`) to ensure valid placements.
- Recursion is used to try placing a queen row by row. If a placement is valid, the state is updated, and the algorithm proceeds to the next row.
- When all rows are filled, the current configuration is added to the result. The algorithm backtracks to explore other possibilities.

[Link to code](./51_n_queens.py)

**Notes**:
- Time complexity: O(N!), where N is the size of the board. This results from trying N options for each row, then N-1 for the next, and so on.
- Space complexity: O(N^2), for the board representation and the recursion stack.


## 78. Subsets

**Description**:
Given a set of distinct integers, nums, return all possible subsets (the power set).

**Example**:
```plaintext
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```

**Solution**:
We use a backtracking approach to explore all subsets. For each element, we decide to either include it in the current subset or exclude it. This allows us to build subsets recursively.

[Link to code](./078_subsets.py)

**Notes**:
- Time complexity: O(2^n), where n is the number of elements in `nums`, as each element can either be included or excluded.
- Space complexity: O(n), for the space used by the recursion stack and storing subsets.

## 46. Permutations

**Description**:
Given an array of distinct integers, return all the possible permutations. You can return the answer in any order.

**Example**:
```plaintext
Input: nums = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

**Solution**:
We use a backtracking approach to explore all permutations. The function recursively adds unused numbers to the current permutation and backtracks when it reaches the length of the input list.

[Link to code](./046_permutations.py)

**Notes**:
- Time complexity: O(n * n!), where n is the length of the input list. Each permutation is generated, and each is stored.
- Space complexity: O(n), for the recursion stack and storage of the result.

## 39. Combination Sum

**Description**:
Given an array of distinct integers `nums` and a target integer `target`, find all unique combinations in `nums` where the numbers sum to `target`. Each number can be used multiple times.

**Example**:
```plaintext
Input: nums = [2, 3, 6, 7], target = 7
Output: [[7], [2, 2, 3]]
Explanation: The number 2 can be used multiple times.
```

**Solution**:
The approach uses backtracking to explore all possible combinations:
- If the sum matches the target, store the combination.
- If the sum exceeds the target, backtrack.
- Recursive calls decide to include or skip a number.

[Link to code](./039_combination_sum.py)

**Notes**:
- Time complexity: O(2^t), where `t` is the target value due to exploring combinations.
- Space complexity: O(t), due to the recursion depth and storing combinations.

## 17. Letter Combinations of a Phone Number

**Description**:
Given a string containing digits from `2-9`, return all possible letter combinations that the number could represent. A mapping of digits to letters (as on the telephone buttons) is used.

**Example**:
```plaintext
Input: digits = "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

**Solution**:
We use backtracking to explore all combinations of letters for the given digits. For each digit, we iterate through its corresponding letters and recursively build combinations until we reach the length of the input digits.

[Link to code](./017_letter_combinations.py)

**Notes**:
- Time complexity: O(4^n), where n is the length of the input digits. Each digit can map to 3 or 4 letters.
- Space complexity: O(n), due to the recursion stack and storing combinations.

## 79. Word Search

**Description**:
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example**:
```plaintext
Input:
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"

Output:
True
```

**Solution**:
This problem can be solved using a backtracking approach. The algorithm starts from each cell of the grid and attempts to match the given word by exploring neighboring cells (up, down, left, right). If the word is found, it returns `True`; otherwise, it continues searching. If at any point the word cannot be matched, it backtracks by restoring the previous state.

**Steps**:
1. Traverse each cell of the grid and attempt to match the word starting from that cell.
2. Use backtracking to explore all four possible directions (up, down, left, right) from the current cell.
3. Mark cells as visited temporarily to avoid reusing the same cell in the current path.
4. If all letters are matched, return `True`.
5. Restore the original cell's value if the current path does not lead to a solution.

[Link to code](./079_word_search.py)

**Notes**:
- Time Complexity: `O(N * M * 3^L)`, where `N * M` is the number of cells in the grid, and `L` is the length of the word. For each cell, we have at most 3 directions to explore (excluding the direction we came from).
- Space Complexity: `O(L)`, where `L` is the length of the word, as we store the recursion stack.