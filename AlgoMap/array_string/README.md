# Problems

| Problem Number | Problem Name                                   | Explanation                                    | Code                                                  |
|----------------|------------------------------------------------|------------------------------------------------|-------------------------------------------------------|
| 2239           | [Find Closest Number to Zero](#2239-find-closest-number-to-zero) | [Explanation](#2239-find-closest-number-to-zero) | [Python Code](./2239_find_closest_number_to_zero.py) |

## 2239. Find Closest Number to Zero

**Description**:
Given an integer array `nums`, return the number with the smallest absolute value. If there are multiple numbers with the same smallest absolute value, return the positive number.

**Example**:
```plaintext
Input:
nums = [-4, -2, 1, 4]

Output: 1
```

**Solution**:
To find the number with the smallest absolute value, iterate through the list while tracking the number with the smallest absolute value. If two numbers have the same smallest absolute value, return the positive number.

[Link to code](2239_find_closest_number_to_zero.py)

**Notes**:
- Time complexity: O(n), where n is the length of the input list `nums`.
- Space complexity: O(1), since no additional space is used beyond a few variables.