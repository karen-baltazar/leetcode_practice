# Problems

| Problem Number | Problem Name      | Explanation                                     | Code                                         |
|----------------|-------------------|-------------------------------------------------|----------------------------------------------|
| 78   | [Subsets](#78-subsets) | [Explanation](#78-subsets) | [Python Code](./078_subsets.py) |
| 46   | [Permutations](#46-permutations)  | [Explanation](#46-permutations) | [Python Code](./046_permutations.py) |
| 77   | [Combinations](#77-combinations)   | [Explanation](#77-combinations) | [Python Code](./077_combinations.py) |
| 39   | [Combination Sum](#39-combination-sum) | [Explanation](#39-combination-sum) | [Python Code](./039_combination_sum.py) |
| 17   | [Letter Combinations of a Phone Number](#17-letter-combinations-of-a-phone-number) | [Explanation](#17-letter-combinations-of-a-phone-number) | [Python Code](./017_letter_combinations.py) |
| 22   | [Generate Parentheses](#22-generate-parentheses) | [Explanation](#22-generate-parentheses) | [Python Code](./022_generate_parentheses.py)      |
| 79   | [Word Search](#79-word-search) | [Explanation](#79-word-search) | [Python Code](./079_word_search.py) |

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

## 77. Combinations

**Description**:
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n]. You can return the answer in any order.

**Example**:
```plaintext
Input: n = 4, k = 2
Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```

**Solution**:
The approach uses backtracking to explore all possible combinations of k elements from 1 to n. It builds combinations recursively by adding elements one at a time and backtracks when the desired combination length is reached.

[Link to code](./077_combinations.py)

**Notes**:
- Time complexity: O(C(n, k)), where C(n, k) is the number of combinations.
- Space complexity: O(k), due to the recursion stack and storing current combinations.

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

## 22. Generate Parentheses

**Description**:
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example**:
```plaintext
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Solution**:
The solution uses backtracking to generate all valid combinations of parentheses. We maintain two counters: one for open parentheses and one for close parentheses. At each step, we decide whether to add an open or close parenthesis based on the current state of these counters. The algorithm ensures that at no point do we have more close parentheses than open ones, which would make the sequence invalid.

[Link to code](022_generate_parentheses.py)

**Notes**:
- Time complexity: O(4^n / sqrt(n)), this is Catalan number time complexity.
- Space complexity: O(n), the space used by the recursion stack.

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