# Problems

| Problem Number | Problem Name                                   | Explanation                                          | Code                                       |
|----------------|------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| 143            | [Reorder List](#143-reorder-list)              | [Explanation](#143-reorder-list)                     | [Python Code](./143_reorder_list.py)       |
| 2            | [Add Two Numbers](#2-add-two-numbers)   | [Explanation](#2-add-two-numbers)            | [Python Code](./002_add_two_numbers.py)      |
| 287            | [Find the Duplicate Number](#287-find-the-duplicate-number) | [Explanation](#287-find-the-duplicate-number)   | [Python Code](./287_find_duplicate.py)       |
| 146            | [LRU Cache](#146-lru-cache)                | [Explanation](#146-lru-cache)                    | [Python Code](./146_lru_cache.py)             |
| 23             | [Merge k Sorted Lists](#23-merge-k-sorted-lists)| [Explanation](#23-merge-k-sorted-lists)              | [Python Code](./023_merge_k_sorted_lists.py)|
| 25             | [Reverse Nodes in k-Group](#25-reverse-nodes-in-k-group) | [Explanation](#25-reverse-nodes-in-k-group)          | [Python Code](./025_reverse_nodes_in_k_group.py)       |
| 206            | [Reverse Linked List](#206-reverse-linked-list)     | [Explanation](#206-reverse-linked-list)            | [Python Code](./206_reverse_linked_list.py)       |
| 21             | [Merge Two Sorted Lists](#21-merge-two-sorted-lists)| [Explanation](#21-merge-two-sorted-lists)         | [Python Code](./021_merge_two_sorted_lists.py)     |
| 141            | [Linked List Cycle](#141-linked-list-cycle)| [Explanation](#141-linked-list-cycle)            | [Python Code](./141_linked_list_cycle.py)        |
| 19             | [Remove Nth Node From End of List](#19-remove-nth-node-from-end-of-list) | [Explanation](#19-remove-nth-node-from-end-of-list) | [Python Code](./019_remove_nth_node_end.py)     |
| 138            | [Copy List with Random Pointer](#138-copy-list-with-random-pointer) | [Explanation](#138-copy-list-with-random-pointer) | [Python Code](./138_copy_list_random_pointer.py) |

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

## 25. Reverse Nodes in k-Group

**Description**:
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. k is a positive integer, and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

**Example**:
```plaintext
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

**Solution**:
The solution uses a helper function to reverse every k nodes in the list. The key idea is to keep track of the next node after the k-group, pass it to the helper function, and directly connect the last node of the reversed group to this next node. This avoids the need for reconnection after reversing the group. The function iteratively processes the list, reversing k nodes at a time, and stops when there are fewer than k nodes left.

[Link to code](./025_reverse_nodes_in_k_group.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the linked list.
- Space complexity: O(1), as the reversal is done in-place without using extra space.

## 206. Reverse Linked List

**Description**:
Given the head of a singly linked list, reverse the list and return the reversed list.

**Example**:
```plaintext
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Solution**:
The solution involves using a dummy node to help reverse the list. We traverse the list, and for each node, we adjust its pointers to place it at the beginning of the reversed list. By maintaining a dummy node as the new head of the reversed list, we can efficiently rearrange the pointers to achieve the reversal. Once the entire list has been traversed and reversed, we return the new head, which is pointed to by the dummy node.

[Link to code](./206_reverse_linked_list.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the linked list.
- Space complexity: O(1), since the reversal is done in place using only a few additional pointers.

## 21. Merge Two Sorted Lists

**Description**:
You are given the heads of two sorted linked lists, `list1` and `list2`. Your task is to merge these two lists into one sorted linked list. The merged list should be made by splicing together the nodes of the first two lists.

**Example**:
```plaintext
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Solution**:
The solution uses a dummy node to simplify the merging process. We iterate through both linked lists, comparing the values of the nodes at the head of each list. We attach the smaller node to the merged list and move the pointer forward in the corresponding list. After one of the lists is exhausted, we attach the remaining nodes from the other list to the merged list. The merged list starts from the node following the dummy node.

[Link to code](./021_merge_two_sorted_lists.py)

**Notes**:
- Time complexity: O(n + m), where n and m are the lengths of `list1` and `list2`, respectively.
- Space complexity: O(1), as we are not using any additional data structures other than a few pointers.

## 141. Linked List Cycle

**Description**:
Given a linked list, determine if it has a cycle in it. A cycle is present if a node's next pointer points to an earlier node in the list, creating a loop.

**Example**:
```plaintext
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the list, where the tail connects to the second node.
```

**Solution**:
The solution employs the two-pointer technique. We use two pointers, `slow` and `fast`. `slow` moves one step at a time, while `fast` moves two steps at a time. If there is a cycle in the list, `slow` and `fast` will eventually meet at some point within the cycle. If `fast` reaches the end of the list (i.e., `fast` or `fast.next` is `None`), then there is no cycle.

[Link to code](./141_linked_list_cycle.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the list.
- Space complexity: O(1), as we are using a constant amount of extra space.

## 19. Remove Nth Node From End of List

**Description**:
Given the head of a linked list, remove the N-th node from the end of the list and return its head. If the list has fewer nodes than `n`, remove the head node.

**Example**:
```plaintext
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Solution**:
To solve this problem, we use a two-pointer technique. We create a dummy node to handle edge cases easily. Both pointers, `left` and `right`, start at the dummy node. We move the `right` pointer `n+1` steps ahead to create a gap of `n` nodes between `left` and `right`. Then, we move both pointers one step at a time until the `right` pointer reaches the end of the list. At this point, the `left` pointer will be right before the node to be removed. We adjust the `next` pointer of the `left` node to skip the node to be removed.

[Link to code](./019_remove_nth_node_end.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the list.
- Space complexity: O(1), as we are using a constant amount of extra space.

## 138. Copy List with Random Pointer

**Description**:
Given a linked list where each node contains an additional random pointer, copy the list. Each node in the original list has two pointers: `next` which points to the next node in the list, and `random` which can point to any node in the list or be `null`. The new list should be a deep copy of the original list.

**Example**:
```plaintext
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**Solution**:
We use a two-pass approach to solve this problem. In the first pass, we create a mapping of each original node to its corresponding new copy node and store these mappings in a dictionary. In the second pass, we set the `next` and `random` pointers for each new node using this mapping. This ensures that we correctly replicate the structure of the original list, including the random pointers.

[Link to code](./138_copy_list_random_pointer.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the list.
- Space complexity: O(n), for storing the node mappings.