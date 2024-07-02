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

## 71. Simplify Path

**Description**:
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period `.` refers to the current directory, a double period `..` refers to the directory up a level, and any multiple consecutive slashes (i.e. `'//'`) are treated as a single slash `'/'`. For this problem, any other format of periods such as `...` are treated as file/directory names.

The canonical path should have the following format:
1. The path starts with a single slash `'/'`.
2. Any two directories are separated by a single slash `'/'`.
3. The path does not end with a trailing `'/'`.
4. The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period `'.'` or double period `'..'`).

**Example**:
```plaintext
Input: path = "/home/"
Output: "/home"

Input: path = "/../"
Output: "/"

Input: path = "/home//foo/"
Output: "/home/foo"
```

**Solution**:
To solve this problem, we use a stack to process each directory in the path. By iterating through the characters in the path, we can build each directory name and decide how to handle it based on the rules given. After processing all directories, we can join the stack to form the canonical path.

[Link to code](20_valid_parentheses.py)

**Notes**:
- Time complexity: O(N), where N is the length of the path. We iterate through the path once.
- Space complexity: O(N), for the stack used to store directory names.