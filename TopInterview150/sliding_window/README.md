# Problems

## 209. Minimum Size Subarray Sum

**Description**:
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray of which the sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.

**Example**:
```plaintext
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```
**Solution**:
To find the minimal length of a subarray with a sum greater than or equal to target, we can use a sliding window approach. The idea is to expand the window by moving the right pointer and then contract it by moving the left pointer until the sum of the window is less than the target. This ensures that we are always checking the smallest possible subarray that meets the condition.

[Link to code](209_minimum_size_sum.py)

**Notes**:
- Time complexity: O(n), where n is the length of the array `nums`.
- Space complexity: O(1), as we are using only a few extra variables.

## 3. Longest Substring Without Repeating Characters

**Description**:
Given a string `s`, find the length of the longest substring without repeating characters.

**Example**:
```plaintext
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Solution**:
To find the length of the longest substring without repeating characters, we can use a sliding window approach with two pointers. We use a set to keep track of the characters in the current window. If a character is repeated, we move the left pointer to the right until the character is no longer in the window.

[Link to code](003_longest_substring.py)

**Notes**:
- Time complexity: O(n), where n is the length of the string.
- Space complexity: O(min(n, m)), where n is the length of the string and m is the character set size.

