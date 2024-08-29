# Problems

| Problem Number | Problem Name                             | Explanation                                    | Code                                      |
|----------------|------------------------------------------|------------------------------------------------|-------------------------------------------|
| 977            | [Squares of a Sorted Array](#977-squares-of-a-sorted-array) | [Explanation](#977-squares-of-a-sorted-array) | [Python Code](./977_squares_of_a_sorted_array.py) |

## 977. Squares of a Sorted Array

**Description**:
Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

**Example**:
```plaintext
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
```

**Solution**:
The solution involves using two pointers, one starting at the beginning (`left`) and the other at the end (`right`) of the array. We compare the absolute values of the elements at these pointers, square the larger one, and move the pointer inward. We store the results in a new list in reverse order to ensure the final array is sorted in non-decreasing order.

[Link to code](977_squares_of_a_sorted_array.py)

**Notes**:
- Time complexity: O(n), where n is the length of the input array.
- Space complexity: O(n), for storing the result.