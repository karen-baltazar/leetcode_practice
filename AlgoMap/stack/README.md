# Problems

| Problem Number | Problem Name                         | Explanation                                      | Code                                              |
|----------------|--------------------------------------|--------------------------------------------------|---------------------------------------------------|
| 20             | [Valid Parentheses](#20-valid-parentheses) | [Explanation](#20-valid-parentheses)             | [Python Code](./020_valid_parentheses.py)           |

## 20. Valid Parentheses

**Description**:
Given a string `s` containing just the characters `'(', ')', '{', '}', '[' and ']'`, determine if the input string is valid. The string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.

**Example**:
```plaintext
Input: s = "()[]{}"
Output: true
```

**Solution**:
The solution involves using a stack to track opening brackets. As we traverse the string, we push opening brackets onto the stack. When we encounter a closing bracket, we check if it matches the top of the stack (i.e., the most recent unmatched opening bracket). If it matches, we pop the stack; otherwise, the string is invalid. If the stack is empty after processing the entire string, the string is valid.

[Link to code](020_valid_parentheses.py)

**Notes**:
- Time complexity: O(n), where n is the length of the input string.
- Space complexity: O(n), for the stack used to store unmatched opening brackets.