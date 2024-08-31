# Problems

| Problem Number | Problem Name                         | Explanation                                      | Code                                              |
|----------------|--------------------------------------|--------------------------------------------------|---------------------------------------------------|
| 22             | [Generate Parentheses](#22-generate-parentheses) | [Explanation](#22-generate-parentheses)          | [Python Code](./022_generate_parentheses.py)      |

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