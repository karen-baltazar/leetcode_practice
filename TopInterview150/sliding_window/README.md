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
Time complexity: O(n), where n is the length of the array `nums`.
Space complexity: O(1), as we are using only a few extra variables.