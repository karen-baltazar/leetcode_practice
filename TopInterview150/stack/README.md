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

[Link to code](020_valid_parentheses.py)

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

[Link to code](071_simplify_path.py)

**Notes**:
- Time complexity: O(N), where N is the length of the path. We iterate through the path once.
- Space complexity: O(N), for the stack used to store directory names.

## 155. Min Stack

**Description**:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the `MinStack` class with the following methods:
- `push(val)`: Pushes the element `val` onto the stack.
- `pop()`: Removes the element on the top of the stack.
- `top()`: Gets the top element of the stack.
- `getMin()`: Retrieves the minimum element in the stack.

**Example**:
```plaintext
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Solution**:
To solve this problem, we use two stacks: one for the actual stack operations and another to keep track of the minimum values. By maintaining the minimum stack, we can ensure that retrieving the minimum value is efficient.

[Link to code](155_min_stack.py)

**Notes**:
- Time complexity for each operation: O(1)
- Space complexity: O(n), where n is the number of elements in the stack.