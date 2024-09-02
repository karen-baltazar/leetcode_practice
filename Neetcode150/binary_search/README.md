# Problems

| Problem Number | Problem Name                                         | Explanation                                      | Code                                          |
|----------------|------------------------------------------------------|--------------------------------------------------|-----------------------------------------------|
| 981            | [Time Based Key-Value Store](#981-time-based-key-value-store) | [Explanation](#981-time-based-key-value-store)   | [Python Code](./981_time_based_key_value_store.py) |
| 4            | [Median of Two Sorted Arrays](#4-median-of-two-sorted-arrays) | [Explanation](#4-median-of-two-sorted-arrays)    | [Python Code](./004_median_of_two_sorted_arrays.py) |


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