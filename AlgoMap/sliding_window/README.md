# Problems

| Problem Number | Problem Name                                   | Explanation                                          | Code                                       |
|----------------|------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| 643            | [Maximum Average Subarray I](#643-maximum-average-subarray-i) | [Explanation](#643-maximum-average-subarray-i)       | [Python Code](./643_maximum_average_subarray.py) |


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