# Problems

| Problem Number | Problem Name                         | Explanation                                      | Code                                              |
|----------------|--------------------------------------|--------------------------------------------------|---------------------------------------------------|
| 22             | [Generate Parentheses](#22-generate-parentheses) | [Explanation](#22-generate-parentheses)          | [Python Code](./022_generate_parentheses.py)      |
| 84             | [Largest Rectangle in Histogram](#84-largest-rectangle-in-histogram) | [Explanation](#84-largest-rectangle-in-histogram) | [Python Code](./084_largest_rectangle_in_histogram.py) |

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