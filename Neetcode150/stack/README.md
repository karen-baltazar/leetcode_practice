# Problems

| Problem Number | Problem Name                         | Explanation                                      | Code                                              |
|----------------|--------------------------------------|--------------------------------------------------|---------------------------------------------------|
| 22             | [Generate Parentheses](#22-generate-parentheses) | [Explanation](#22-generate-parentheses)          | [Python Code](./022_generate_parentheses.py)      |
| 84             | [Largest Rectangle in Histogram](#84-largest-rectangle-in-histogram) | [Explanation](#84-largest-rectangle-in-histogram) | [Python Code](./084_largest_rectangle_in_histogram.py) |
| 853            | [Car Fleet](#853-car-fleet)          | [Explanation](#853-car-fleet)                    | [Python Code](./853_car_fleet.py)                 |
| 20             | [Valid Parentheses](#20-valid-parentheses) | [Explanation](#20-valid-parentheses)             | [Python Code](./020_valid_parentheses.py)           |
| 150            | [Evaluate Reverse Polish Notation](#150-evaluate-reverse-polish-notation) | [Explanation](#150-evaluate-reverse-polish-notation) | [Python Code](./150_evaluate_reverse_polish_notation.py) |
| 739            | [Daily Temperatures](#739-daily-temperatures) | [Explanation](#739-daily-temperatures)           | [Python Code](./739_daily_temperatures.py)        |
| 155            | [Min Stack](#155-min-stack)          | [Explanation](#155-min-stack)                    | [Python Code](./155_min_stack.py)                 |

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

## 84. Largest Rectangle in Histogram

**Description**:
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

**Example**:
```plaintext
Input: heights = [2,1,5,6,2,3]
Output: 10
```

**Solution**:
The solution uses a stack-based approach to efficiently calculate the maximum rectangular area. Here's a step-by-step explanation:

1. **Add a zero at the end**: We append a `0` to the `heights` array. This ensures that all bars in the histogram are processed correctly, even if the largest rectangle spans to the end of the array.

2. **Using a stack**: We use a stack to store pairs of `(index, height)`. As we iterate through the bars, we compare the current bar's height with the height at the top of the stack.
   - If the current bar is shorter, it means the rectangle formed by the bar at the top of the stack can't be extended further. We pop the stack and calculate the area using the popped height, considering it as the smallest height of a rectangle.
   - The width of this rectangle is determined by the difference between the current index and the index of the bar that was at the top of the stack before the current bar.

3. **Updating `start_index`**: If we pop a bar from the stack, the `start_index` is updated to reflect the index of this popped bar. This ensures that the width of the next rectangle considers all bars up to the current one.

4. **Calculating the maximum area**: The variable `max_area` keeps track of the largest rectangle found as we process each bar. After iterating through all bars, `max_area` will hold the area of the largest possible rectangle in the histogram.

[Link to code](084_largest_rectangle_in_histogram.py)

**Notes**:
- Time complexity: O(n), where n is the number of bars in the histogram.
- Space complexity: O(n), for the stack.

## 853. Car Fleet

**Description**:
Given the position and speed of cars heading towards the same target, determine how many car fleets will arrive at the destination.

**Example**:
```plaintext
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
```

**Solution**:
To solve this problem, we start by pairing each car's position with its speed, and then sort these pairs by position in descending order so that we process cars starting from the closest to the target. For each car, we calculate the time it will take to reach the target and track these times using a stack. If a car's time to reach the target is less than or equal to the time of the car in front of it, it means the current car will catch up and merge into the same fleet as the car ahead. Thus, we only count it as one fleet. The number of fleets that will eventually reach the target is the number of distinct times left in the stack after processing all cars.

[Link to code](./853_car_fleet.py)

**Notes**:
- Time complexity: O(n log n), where n is the number of cars. The sorting step takes O(n log n) time, and iterating through the cars takes O(n) time.
- Space complexity: O(n), for the stack used to store the time each car takes to reach the target.

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

## 155. Min Stack

**Description**:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

**Example**:
```plaintext
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // Returns -3
minStack.pop();
minStack.top();    // Returns 0
minStack.getMin(); // Returns -2
```

**Solution**:
The solution uses two stacks: a main stack to store all the values and a min stack to keep track of the minimum values. Every time we push a value, we also check if it's the new minimum. If it is, we push it onto the min stack. When we pop a value, we check if it's the current minimum, and if so, we pop it from the min stack as well. This allows us to get the minimum value in constant time.

[Link to code](155_min_stack.py)

**Notes**:
- Time complexity: O(1) for all operations.
- Space complexity: O(n), where n is the number of elements in the stack.