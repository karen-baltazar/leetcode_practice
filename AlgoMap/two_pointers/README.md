# Problems

| Problem Number | Problem Name                             | Explanation                                    | Code                                      |
|----------------|------------------------------------------|------------------------------------------------|-------------------------------------------|
| 977            | [Squares of a Sorted Array](#977-squares-of-a-sorted-array) | [Explanation](#977-squares-of-a-sorted-array) | [Python Code](./977_squares_of_a_sorted_array.py) |
| 344            | [Reverse String](#344-reverse-string)    | [Explanation](#344-reverse-string)            | [Python Code](./344_reverse_string.py)    |

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

## 344. Reverse String

**Description**:  
Given a list of characters `s`, reverse the list in-place.

**Example**:
```plaintext
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Solution**:  
The solution involves using two pointers, `start` and `end`, which initially point to the beginning and end of the list, respectively. We swap the characters at these pointers and then move the pointers towards each other until they meet or cross. This process effectively reverses the list in-place.

[Link to code](344_reverse_string.py)

**Notes**:
- Time complexity: O(n), where n is the length of the list.
- Space complexity: O(1), as the reversal is done in-place.