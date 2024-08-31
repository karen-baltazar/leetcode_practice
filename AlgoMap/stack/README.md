# Problems

| Problem Number | Problem Name                         | Explanation                                      | Code                                              |
|----------------|--------------------------------------|--------------------------------------------------|---------------------------------------------------|
| 20             | [Valid Parentheses](#20-valid-parentheses) | [Explanation](#20-valid-parentheses)             | [Python Code](./020_valid_parentheses.py)           |
| 682            | [Baseball Game](#682-baseball-game)  | [Explanation](#682-baseball-game)                | [Python Code](./682_baseball_game.py)              |
| 150            | [Evaluate Reverse Polish Notation](#150-evaluate-reverse-polish-notation) | [Explanation](#150-evaluate-reverse-polish-notation) | [Python Code](./150_evaluate_reverse_polish_notation.py) |
| 739            | [Daily Temperatures](#739-daily-temperatures) | [Explanation](#739-daily-temperatures)           | [Python Code](./739_daily_temperatures.py)        |

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

## 150. Evaluate Reverse Polish Notation

**Description**:
Evaluate the value of an arithmetic expression in Reverse Polish Notation. The valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

Note:
- Division between two integers should truncate toward zero.
- The input tokens are always valid Reverse Polish Notation.

**Example**:
```plaintext
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

**Solution**:
The solution uses a stack to keep track of operands. When an operator is encountered, the top two elements are popped from the stack, the operation is performed, and the result is pushed back onto the stack. The final result is the only element remaining in the stack.

[Link to code](150_evaluate_reverse_polish_notation.py)

**Notes**:
- Time complexity: O(n), where n is the number of tokens.
- Space complexity: O(n), for storing the stack.

## 739. Daily Temperatures

**Description**:
Given a list of daily temperatures `temperatures`, return a list `result` such that `result[i]` is the number of days you have to wait after the `i-th` day to get a warmer temperature. If there is no future day for which this is possible, put `0` instead.

**Example**:
```plaintext
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

**Solution**:
The solution uses a stack to keep track of temperatures and their indices as we iterate through the list. For each temperature, if it is warmer than the temperature at the top of the stack, we calculate the difference in days and pop the stack. We continue this process until the stack is empty or the current temperature is not warmer than the temperature at the top of the stack. If there are any remaining temperatures in the stack, they are automatically assigned a `0` because no warmer day exists after them.

[Link to code](739_daily_temperatures.py)

**Notes**:
- Time complexity: O(n), where n is the length of the input list.
- Space complexity: O(n), for the stack used to store temperatures and indices.