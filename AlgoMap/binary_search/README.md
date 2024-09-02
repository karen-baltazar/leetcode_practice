# Problems

| Problem Number | Problem Name                               | Explanation                                      | Code                                          |
|----------------|--------------------------------------------|--------------------------------------------------|-----------------------------------------------|
| 704            | [Binary Search](#704-binary-search)         | [Explanation](#704-binary-search)                | [Python Code](./704_binary_search.py)         |
| 35             | [Search Insert Position](#35-search-insert-position) | [Explanation](#35-search-insert-position)        | [Python Code](./035_search_insert_position.py)   |
| 278            | [First Bad Version](#278-first-bad-version)          | [Explanation](#278-first-bad-version)            | [Python Code](./278_first_bad_version.py)      |

## 704. Binary Search

**Description**:
Given a sorted array of integers `nums` and a target value `target`, implement a binary search to find the target's index in the array. If the target does not exist in the array, return `-1`.

**Example**:
```plaintext
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 is found at index 4.
```

**Solution**:
Binary search is a classic algorithm that repeatedly divides the search interval in half. Starting with the entire array, it compares the middle element to the target. If the middle element is the target, the search is successful. If the target is greater, it eliminates the left half, and if it's smaller, it eliminates the right half, continuing the process until the target is found or the search space is exhausted.

[Link to code](./704_binary_search.py)

**Notes**:
- Time complexity: O(log n), where n is the number of elements in the array.
- Space complexity: O(1), as the search is performed in place without additional memory.

## 35. Search Insert Position

**Description**:
Given a sorted array of integers `nums` and a target value `target`, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

**Example**:
```plaintext
Input: nums = [1,3,5,6], target = 5
Output: 2
Explanation: 5 is found at index 2.
```

**Solution**:
This problem is essentially a variation of binary search. The idea is to use the standard binary search approach to locate the target. If found, return the index. If not, return the index where it should be inserted to maintain the sorted order.

[Link to code](./035_search_insert_position.py)

**Notes**:
- Time complexity: O(log n), where n is the number of elements in the array.
- Space complexity: O(1), as the search is performed in place without additional memory.

## 278. First Bad Version

**Description**:
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version fails the quality check. Since each version is developed based on the previous one, all the following versions are also faulty.

Given `n` versions [1, 2, ..., n], you need to find out the first bad one, which causes all the following ones to be bad. You have an API `isBadVersion(version)` that returns whether a version is bad. Implement a function to find the first bad version by making the minimum number of API calls.

**Example**:
```plaintext
Input: n = 5, bad = 4
Output: 4
Explanation: The first bad version is 4.
```

**Solution**:
The problem can be efficiently solved using binary search. The goal is to minimize the number of calls to the `isBadVersion` API by dividing the search space in half. Once a bad version is found, we check if it's the first bad version by verifying the previous version. If it is, we return it; otherwise, we continue searching in the left half.

[Link to code](./278_first_bad_version.py)

**Notes**:
- Time complexity: O(log n), where n is the total number of versions.
- Space complexity: O(1), as the search is done in place without additional memory.