# Problems

## 20. Valid Parentheses

**Description**:
Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

**Example**:
```plaintext
Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
```
**Solution**:
To solve this problem, we use a stack to keep track of the opening brackets. For each closing bracket, we check if it matches the most recent opening bracket on the stack. If it does, we pop the opening bracket from the stack. If it does not, the string is not valid. At the end, if the stack is empty, all brackets were matched correctly.

[Link to code](20_valid_parentheses.py)

**Notes**:
- Time complexity: O(N), where N is the length of the string. We iterate through the string once.
- Space complexity: O(N), in the worst case, we might store all opening brackets in the stack.