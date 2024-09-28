# Problems

| Problem Number | Problem Name                      | Explanation                                           | Code                                            |
|----------------|-----------------------------------|-------------------------------------------------------|-------------------------------------------------|
| 90  | [Subsets II](#90-subsets-ii)     | [Explanation](#90-subsets-ii) | [Python Code](./090_subsets_ii.py) |
| 40  | [Combination Sum II](#40-combination-sum-ii) | [Explanation](#40-combination-sum-ii) | [Python Code](./040_combination_sum_ii.py) |
| 131 | [Palindrome Partitioning](#131-palindrome-partitioning) | [Explanation](#131-palindrome-partitioning)       | [Python Code](./131_palindrome_partitioning.py) |
| 51  | [N-Queens](#51-n-queens) | [Explanation](#51-n-queens) | [Python Code](./051_n_queens.py) |

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