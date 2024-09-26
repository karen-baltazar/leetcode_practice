# Problems

| Problem Number | Problem Name                                   | Explanation                                      | Code                                           |
|----------------|------------------------------------------------|--------------------------------------------------|------------------------------------------------|
| 1046 | [Last Stone Weight](#1046-last-stone-weight) | [Explanation](#1046-last-stone-weight)         | [Python Code](./1046_last_stone_weight.py)  |
| 215  | [Kth Largest Element in an Array](#215-kth-largest-element-in-an-array) | [Explanation](#215-kth-largest-element-in-an-array) | [Python Code](./215_kth_largest_element.py)      |
| 347  | [Top K Frequent Elements](#347-top-k-frequent-elements) | [Explanation](#347-top-k-frequent-elements)    | [Python Code](./347_top_k_frequent_elements.py)  |
| 973  | [K Closest Points to Origin](#973-k-closest-points-to-origin) | [Explanation](#973-k-closest-points-to-origin) | [Python Code](./973_k_closest_points.py)         |
| 23   | [Merge k Sorted Lists](#23-merge-k-sorted-lists) | [Explanation](#23-merge-k-sorted-lists) | [Python Code](./023_merge_k_sorted_lists.py) |

## 1046. Last Stone Weight

**Description**:
You are given an array of integers `stones` where `stones[i]` is the weight of the i-th stone. Smash the two heaviest stones together. If they have the same weight, both are destroyed; if not, the heavier stone is reduced by the lighter stone's weight. Return the weight of the last remaining stone or 0 if none are left.

**Example**:
```plaintext
Input: stones = [2,7,4,1,8,1]
Output: 1
```

**Solution**:
We use a max-heap to track the heaviest stones. By negating the weights, we can utilize Python's min-heap. We repeatedly pop the two heaviest stones and push the difference back into the heap until one or no stones remain.

[Link to code](./1046_last_stone_weight.py)

**Notes**:
- Time complexity: O(n log n). This arises from the need to heapify the list and perform heap operations (push and pop), which each take O(log n) time.
- Space complexity: O(n) due to storing the stones in the heap.

## 215. Kth Largest Element in an Array

**Description**:
Given an integer array `nums` and an integer `k`, return the k-th largest element in the array. Note that it is the k-th largest element in sorted order, not the k-th distinct element.

**Example**:
```plaintext
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Solution**:
To find the k-th largest element, we use a min-heap of size `k`. We iterate through the array, maintaining the heap with only the k largest elements. At the end, the root of the heap (the smallest in the heap) is the k-th largest element.

[Link to code](./215_kth_largest_element.py)

**Notes**:
- Time complexity: O(n log k). Each insertion and removal operation in the heap takes O(log k), and we do this for all `n` elements.
- Space complexity: O(k) for the heap that stores the k largest elements.

## 347. Top K Frequent Elements

**Description**:
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Example**:
```plaintext
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Solution**:
The solution employs a bucket sort approach. After counting the frequency of each number, elements are placed into frequency-based buckets. We then collect elements starting from the highest frequency bucket, stopping once we have gathered `k` elements.

[Link to code](./347_top_k_frequent_elements.py)

**Notes**:
- Time complexity: O(n). Counting frequencies and iterating through the buckets are linear operations.
- Space complexity: O(n), as extra space is used for the frequency map and buckets.

## 973. K Closest Points to Origin

**Description**:
Given an array of points where `points[i] = [x, y]` represents a point on the X-Y plane, return the `k` closest points to the origin (0, 0).

**Example**:
```plaintext
Input: points = [[1,3],[-2,2],[5,8],[0,1]], k = 2
Output: [[-2,2],[1,3]]
```

**Solution**:
The approach uses a min-heap to maintain the closest points. The distance to the origin is calculated, and points are pushed into the heap. If the heap exceeds size `k`, the farthest point is removed. The resulting heap contains the `k` closest points.

[Link to code](./973_k_closest_points.py)

**Notes**:
- Time complexity: O(n log k), where n is the number of points. Each insertion into the heap takes log k time.
- Space complexity: O(k) for storing the k closest points.

## 23. Merge k Sorted Lists

**Description**:
Merge `k` sorted linked lists and return it as one sorted list. The linked lists are represented as arrays of `ListNode`.

**Example**:
```plaintext
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**Solution**:
This approach uses a min-heap to efficiently merge the lists. The heap is initialized with the first node of each list. The smallest node is repeatedly popped from the heap, and its next node is pushed into the heap until all nodes are merged.

[Link to code](./023_merge_k_sorted_lists.py)

**Notes**:
- Time complexity: O(n log k), where `n` is the total number of nodes across all lists. Each insertion and removal operation from the heap takes log k time.
- Space complexity: O(k) for storing the nodes in the heap.