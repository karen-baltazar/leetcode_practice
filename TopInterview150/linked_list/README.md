# Problems

## 141. Linked List Cycle

**Description**:
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (0-indexed) in the linked list where the tail connects to. If `pos` is `-1`, then there is no cycle in the linked list.

**Example**:
```plaintext
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

**Solution**:
We use Floyd's Tortoise and Hare algorithm to detect a cycle in the linked list. We initialize two pointers, slow and fast, both starting at the head of the list. The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. If there is a cycle, the slow and fast pointers will eventually meet. If the fast pointer reaches the end of the list, there is no cycle.

[Link to code](141_linked_list_cycle.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the list.
- Space complexity: O(1), as no additional space is used.