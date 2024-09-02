# Problems

| Problem Number | Problem Name                                         | Explanation                                      | Code                                          |
|----------------|------------------------------------------------------|--------------------------------------------------|-----------------------------------------------|
| 981            | [Time Based Key-Value Store](#981-time-based-key-value-store) | [Explanation](#981-time-based-key-value-store)   | [Python Code](./981_time_based_key_value_store.py) |
| 4            | [Median of Two Sorted Arrays](#4-median-of-two-sorted-arrays) | [Explanation](#4-median-of-two-sorted-arrays)    | [Python Code](./004_median_of_two_sorted_arrays.py) |
| 704            | [Binary Search](#704-binary-search)         | [Explanation](#704-binary-search)                | [Python Code](./704_binary_search.py)         |
| 74            | [Search a 2D Matrix](#74-search-a-2d-matrix) | [Explanation](#74-search-a-2d-matrix) | [Python Code](./074_search_2d_matrix.py) |
| 153            | [Find Minimum in Rotated Sorted Array](#153-find-minimum-in-rotated-sorted-array) | [Explanation](#153-find-minimum-in-rotated-sorted-array) | [Python Code](./153_min_in_rotated_array.py) |
| 33             | [Search in Rotated Sorted Array](#33-search-in-rotated-sorted-array) | [Explanation](#33-search-in-rotated-sorted-array) | [Python Code](./033_search_rotated_array.py) |
| 875            | [Koko Eating Bananas](#875-koko-eating-bananas)       | [Explanation](#875-koko-eating-bananas)          | [Python Code](./875_koko_eating_bananas.py)   |

## 981. Time Based Key-Value Store

**Description**:
Design a time-based key-value store that supports setting and retrieving values based on keys and timestamps. Implement two functions:
1. `set(key, value, timestamp)`: Stores the key-value pair with the given timestamp.
2. `get(key, timestamp)`: Retrieves the value corresponding to the key such that the timestamp is less than or equal to the given timestamp.

**Example**:
```plaintext
Input: 
TimeMap kv = new TimeMap();
kv.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
kv.get("foo", 1);         // output "bar"
kv.get("foo", 3);         // output "bar", since "bar" is the latest value before timestamp 3.
kv.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
kv.get("foo", 4);         // output "bar2"
kv.get("foo", 5);         // output "bar2"
```

**Solution**:
The key idea is to store the values along with their timestamps in a dictionary where each key maps to a list of `[value, timestamp]` pairs. To efficiently retrieve the correct value for a given timestamp, binary search is employed. The `get` method performs a binary search to find the latest timestamp that is less than or equal to the given timestamp and returns the corresponding value.

[Link to code](./981_time_based_key_value_store.py)

**Notes**:
- Time complexity:
  - `set`: O(1) for inserting the key-value pair.
  - `get`: O(log n), where `n` is the number of timestamps for the key. Binary search efficiently finds the correct value.
- Space complexity: O(n), where `n` is the number of `set` operations since each one stores a new key-value pair with its timestamp.

## 4. Median of Two Sorted Arrays

**Description**:
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be `O(log (m+n))`.

**Example**:
```plaintext
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.0
Explanation: Combined array is [1, 2, 3] and median is 2.0.

Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
Explanation: Combined array is [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.
```

**Solution**:
To find the median of two sorted arrays, we use a binary search strategy. The key is to partition both arrays such that all elements on the left side of the partition are less than or equal to all elements on the right side. We only need to perform the binary search on the smaller array to find the correct partition, which optimizes the search.

If the total number of elements is odd, the median is the middle element. If it is even, the median is the average of the two middle elements.

[Link to code](./004_median_of_two_sorted_arrays.py)

**Notes**:
- Time complexity: O(log(min(m, n))), where `m` and `n` are the lengths of the input arrays.
- Space complexity: O(1), since the algorithm only uses a constant amount of extra space.

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

## 74. Search a 2D Matrix

**Description**:
Write an efficient algorithm that searches for a target value in an m x n integer matrix. This matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

**Example**:
```plaintext
Input: matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]], target = 5
Output: True
Explanation: 5 is present in the matrix.

Input: matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]], target = 20
Output: False
Explanation: 20 is not present in the matrix.
```

**Solution**:
To search for the target value in the 2D matrix, we use a two-step approach:
1. **Row Identification**: Iterate through the rows to find the row that may contain the target. We check if the target is within the range of the current row.
2. **Binary Search**: Once the potential row is identified, perform a binary search in that row to find the target value. 

The binary search is performed within the identified row, leveraging the sorted nature of the matrix rows.

[Link to code](./074_search_2d_matrix.py)

**Notes**:
- Time complexity: O(log(m * n)), where m is the number of rows and n is the number of columns. Binary search is performed on the combined elements of the matrix.
- Space complexity: O(1), as only a constant amount of extra space is used.

## 153. Find Minimum in Rotated Sorted Array

**Description**:
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]` after rotating it 4 times. Given the rotated array `nums`, return the minimum element in the array. You must write an algorithm that runs in `O(log n)` time.

**Example**:
```plaintext
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The minimum value is 0, which is at the index 4.
```

**Solution**:
To find the minimum element in a rotated sorted array, we can use a binary search approach. The idea is to compare the middle element with the rightmost element. If the middle element is greater than the rightmost element, the minimum must lie in the right half. Otherwise, it lies in the left half. This way, we continuously narrow down the search space until we find the minimum element.

[Link to code](./153_min_in_rotated_array.py)

**Notes**:
- Time complexity: O(log n), where n is the number of elements in the array.
- Space complexity: O(1), as only a constant amount of extra space is used.

## 33. Search in Rotated Sorted Array

**Description**:
You are given a rotated sorted array where the rotation point is unknown. Write a function to search for a given target in the array and return its index. If the target is not found, return `-1`. The solution must run in `O(log n)` time complexity.

**Example**:
```plaintext
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Explanation: 0 is found at index 4.
```

**Solution**:
The problem can be solved in two phases:
1. First, find the smallest element, which serves as the rotation point using binary search.
2. After determining the rotation point, perform another binary search in the appropriate subarray based on the target's value.

[Link to code](./033_search_rotated_array.py)

**Notes**:
- Time complexity: O(log n), since both steps use binary search.
- Space complexity: O(1), as only a constant amount of extra space is used.

## 875. Koko Eating Bananas

**Description**:
Koko loves to eat bananas, but she can only eat at most one pile per hour. There are `n` piles of bananas, and she has `h` hours to finish all the bananas. Each hour, Koko chooses a pile and eats bananas at a fixed speed of `k` bananas per hour. Determine the minimum integer speed `k` that allows her to eat all the bananas within `h` hours.

**Example**:
```plaintext
Input: piles = [3,6,7,11], h = 8
Output: 4
Explanation: Koko can eat at a speed of 4 bananas per hour to finish all piles within 8 hours.

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Explanation: Koko must eat at a speed of 30 bananas per hour to finish all piles within 5 hours.
```

**Solution**:
The problem is solved using binary search to find the minimum speed `k`. The approach involves:
1. Searching through potential speeds between 1 and the size of the largest pile.
2. Using a helper function to determine if a given speed allows Koko to finish eating all bananas within `h` hours.
3. Narrowing down the speed range based on whether the current speed is sufficient or not.

[Link to code](./875_koko_eating_bananas.py)

**Notes**:
- Time complexity: O(n log m), where `n` is the number of piles and `m` is the maximum number of bananas in a pile. This is because the binary search operates over a range of `m` possible speeds, and each check involves iterating over `n` piles.
- Space complexity: O(1), since only a constant amount of extra space is used.