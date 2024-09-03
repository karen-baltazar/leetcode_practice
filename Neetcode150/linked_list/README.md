# Problems

| Problem Number | Problem Name                                   | Explanation                                          | Code                                       |
|----------------|------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| 143            | [Reorder List](#143-reorder-list)              | [Explanation](#143-reorder-list)                     | [Python Code](./143_reorder_list.py)       |
| 2            | [Add Two Numbers](#2-add-two-numbers)   | [Explanation](#2-add-two-numbers)            | [Python Code](./002_add_two_numbers.py)      |
| 287            | [Find the Duplicate Number](#287-find-the-duplicate-number) | [Explanation](#287-find-the-duplicate-number)   | [Python Code](./287_find_duplicate.py)       |
| 146            | [LRU Cache](#146-lru-cache)                | [Explanation](#146-lru-cache)                    | [Python Code](./146_lru_cache.py)             |
| 23             | [Merge k Sorted Lists](#23-merge-k-sorted-lists)| [Explanation](#23-merge-k-sorted-lists)              | [Python Code](./023_merge_k_sorted_lists.py)|

## 143. Reorder List

**Description**:
Given the head of a singly linked list, reorder the list so that it follows this specific order: first node, last node, second node, second-last node, and so on. The reordering should be done in-place without altering the values, only changing the node pointers.

**Example**:
```plaintext
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

**Solution**:
The solution can be approached in two main steps. First, find the middle of the linked list. Once the middle is identified, reverse the second half of the list. Finally, merge the two halves together, alternating the nodes from each half to achieve the desired order.

[Link to code](./143_reorder_list.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the linked list.
- Space complexity: O(1), as the reordering is done in-place without using additional space.

## 2. Add Two Numbers

**Description**:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

**Example**:
```plaintext
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Solution**:
We traverse both linked lists simultaneously, adding corresponding digits. If the sum of the digits is 10 or more, we keep track of the carry to add to the next pair of digits. The process continues until both lists are fully traversed and there is no remaining carry. The resulting sum is stored in a new linked list.

[Link to code](./002_add_two_numbers.py)

**Notes**:
- Time complexity: O(n), where n is the length of the longer linked list.
- Space complexity: O(1), as we only use a constant amount of extra space (not counting the output list).

## 287. Find the Duplicate Number

**Description**:
Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive, return the duplicate number. You must solve the problem without modifying the array and use only constant extra space.

**Example**:
```plaintext
Input: nums = [1,3,4,2,2]
Output: 2
Explanation: The duplicate number is 2.
```

**Solution**:
The problem can be solved using Floyd's Tortoise and Hare (Cycle Detection) algorithm. The array can be interpreted as a linked list where each index points to the next node. By using two pointers (a slow and a fast pointer), we can detect the cycle and eventually find the duplicate number which is the entrance of the cycle.

[Link to code](./287_find_duplicate.py)

**Notes**:
- Time complexity: O(n), where n is the number of elements in the array.
- Space complexity: O(1), as we only use a constant amount of extra space.

## 146. LRU Cache

**Description**:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. Implement the `LRUCache` class:
- `LRUCache(int capacity)` Initializes the LRU cache with positive size `capacity`.
- `int get(int key)` Returns the value of the key if it exists, otherwise returns `-1`.
- `void put(int key, int value)` Updates the value of the key if it exists. Otherwise, adds the key-value pair to the cache. If the number of keys exceeds the capacity, remove the least recently used key.

**Example**:
```plaintext
Input:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // Cache is {1=1}
lRUCache.put(2, 2); // Cache is {1=1, 2=2}
lRUCache.get(1);    // Returns 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, Cache is {1=1, 3=3}
lRUCache.get(2);    // Returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, Cache is {4=4, 3=3}
lRUCache.get(1);    // Returns -1 (not found)
lRUCache.get(3);    // Returns 3
lRUCache.get(4);    // Returns 4
```

**Solution**:
This solution uses a combination of a doubly linked list and a hash map to keep track of the order of access and the contents of the cache. The doubly linked list allows for efficient reordering of elements (O(1) for insertion and deletion), while the hash map allows for fast access to the elements (O(1) for retrieval and insertion). This ensures that both the `get` and `put` operations run in constant time.

[Link to code](./146_lru_cache.py)

**Notes**:
- Time complexity: O(1) for both `get` and `put` operations.
- Space complexity: O(capacity), where `capacity` is the maximum number of elements in the cache.

## 23. Merge k Sorted Lists

**Description**:
Given an array of `k` linked lists, where each list is sorted in ascending order, merge all the lists into one sorted linked list and return it.

**Example**:
```plaintext
Input: [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**Solution**:
The solution to this problem employs a divide-and-conquer strategy. Here's how it works:
1. **Divide**: We pair up each list and merge them using a helper function that merges two sorted lists.
2. **Conquer**: Continue merging in pairs until only one list remains.

This method is efficient because it repeatedly merges two lists, reducing the overall time complexity.

**Notes**:
- Time complexity: O(N log k), where N is the total number of nodes across all k lists, and k is the number of lists.
- Space complexity: O(1) extra space, not counting the space needed to store the final merged linked list.