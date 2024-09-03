# Problems

| Problem Number | Problem Name                                   | Explanation                                          | Code                                       |
|----------------|------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| 643            | [Maximum Average Subarray I](#643-maximum-average-subarray-i) | [Explanation](#643-maximum-average-subarray-i)       | [Python Code](./643_maximum_average_subarray.py) |
| 1004           | [Max Consecutive Ones III](#1004-max-consecutive-ones-iii) | [Explanation](#1004-max-consecutive-ones-iii)        | [Python Code](./1004_max_consecutive_ones_iii.py) |

## 643. Maximum Average Subarray I

**Description**:
Given an integer array `nums` and an integer `k`, find the contiguous subarray of length `k` that has the maximum average value, and return this value.

**Example**:
```plaintext
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
```

**Solution**:
The solution uses a sliding window approach. Initially, the sum of the first `k` elements is calculated. Then, as the window slides through the array, the sum is adjusted by subtracting the element that leaves the window and adding the element that enters. The maximum sum encountered during this process is recorded, and the maximum average is obtained by dividing this sum by `k`.

[Link to code](./643_maximum_average_subarray.py)

**Notes**:
- Time complexity: O(n), where n is the number of elements in the array.
- Space complexity: O(1), as only a few variables are used for the sliding window calculation.

## 1004. Max Consecutive Ones III

**Description**:
Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`s in the array if you can flip at most `k` `0`s.

**Example**:
```plaintext
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
```

**Solution**:
The solution uses a sliding window approach. We expand the window by moving the `right` pointer across the array and count the number of `0`s encountered. If the count of `0`s exceeds `k`, we shrink the window from the left by moving the `left` pointer until the number of `0`s is back within the allowed limit. The length of the longest valid window gives the desired result.

[Link to code](./1004_max_consecutive_ones_iii.py)

**Notes**:
- Time complexity: O(n), where n is the length of the array.
- Space complexity: O(1), as only a few variables are used to track the window and the count of zeros.