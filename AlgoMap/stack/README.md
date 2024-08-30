# Problems

| Problem Number | Problem Name                         | Explanation                                      | Code                                              |
|----------------|--------------------------------------|--------------------------------------------------|---------------------------------------------------|
| 20             | [Valid Parentheses](#20-valid-parentheses) | [Explanation](#20-valid-parentheses)             | [Python Code](./020_valid_parentheses.py)           |
| 682            | [Baseball Game](#682-baseball-game)  | [Explanation](#682-baseball-game)                | [Python Code](./682_baseball_game.py)              |

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

## 682. Baseball Game

**Description**:
You're keeping score for a baseball game with a list of operations. Each operation is either an integer, `+`, `D`, or `C`:
- An integer represents a score of a new round.
- `+` represents the score for this round as the sum of the last two valid scores.
- `D` represents the score for this round as double the last valid score.
- `C` represents that the last valid score was invalidated and should be removed.

Return the sum of all the valid scores after performing all the operations.

**Example**:
```plaintext
Input: operations = ["5","2","C","D","+"]
Output: 30
```

**Solution**:
The solution uses a list as a record of scores, where each element represents a valid round. The operations are processed sequentially, modifying the record based on the rules provided. The final score is the sum of all elements in the record.

[Link to code](682_baseball_game.py)

**Notes**:
- Time complexity: O(n), where n is the number of operations.
- Space complexity: O(n), for storing the scores in the list.