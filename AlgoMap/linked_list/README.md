# Problems

| Problem Number | Problem Name                                        | Explanation                                        | Code                                              |
|----------------|-----------------------------------------------------|----------------------------------------------------|---------------------------------------------------|
| 83             | [Remove Duplicates from Sorted List](#83-remove-duplicates-from-sorted-list) | [Explanation](#83-remove-duplicates-from-sorted-list) | [Python Code](./083_remove_duplicates_from_sorted_list.py) |

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
