# Problems

| Problem Number | Problem Name                                        | Explanation                                        | Code                                              |
|----------------|-----------------------------------------------------|----------------------------------------------------|---------------------------------------------------|
| 83             | [Remove Duplicates from Sorted List](#83-remove-duplicates-from-sorted-list) | [Explanation](#83-remove-duplicates-from-sorted-list) | [Python Code](./083_remove_duplicates_from_sorted_list.py) |
| 206            | [Reverse Linked List](#206-reverse-linked-list)     | [Explanation](#206-reverse-linked-list)            | [Python Code](./206_reverse_linked_list.py)       |

## 83. Remove Duplicates from Sorted List

**Description**:
Given the head of a sorted linked list, remove all duplicates such that each element appears only once. Return the linked list sorted as well.

**Solution**:
The solution involves traversing the linked list while checking if the current node has the same value as the next node. If a duplicate is found, the next pointer of the current node is adjusted to skip the duplicate node. This process is repeated until the entire list is traversed. As the list is sorted, all duplicates will be adjacent, so adjusting the next pointers is sufficient to remove them.

**Example**:
```plaintext
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the linked list.
- Space complexity: O(1), since no additional data structures are used; only pointers are adjusted.

[Link to code](./083_remove_duplicates_from_sorted_list.py)

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

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the linked list.
- Space complexity: O(1), since the reversal is done in place using only a few additional pointers.

[Link to code](./206_reverse_linked_list.py)