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

## 2. Add Two Numbers

**Description**:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example**:
```plaintext
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Solution**:
To solve this problem, we traverse both linked lists while adding the corresponding digits along with any carry from the previous addition. We use a dummy node to simplify the construction of the result list. If the sum of the digits is 10 or more, we carry over the extra value to the next addition.

[Link to code](002_add_two_numbers.py)

**Notes**:
- Time complexity: O(max(n, m)), where n and m are the lengths of the input lists.
- Space complexity: O(max(n, m)), for the space required by the result list.

## 21. Merge Two Sorted Lists

**Description**:
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

**Example**:
```plaintext
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Solution**:
To solve this problem, we use a dummy node to simplify the construction of the merged list. We compare the current nodes of both input lists and attach the smaller node to the merged list. We continue this process until one of the lists is exhausted. Finally, we attach any remaining nodes from the non-exhausted list to the merged list.

[Link to code](021_merge_two_sorted_lists.py)

**Notes**:
- Time complexity: O(n + m), where n and m are the lengths of the input lists.
- Space complexity: O(1), as the merged list is constructed in-place.

## 19. Remove Nth Node From End of List

**Description**:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

**Example**:
```plaintext
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Explanation: Given linked list: 1->2->3->4->5, the 2nd node from the end is 4, so we remove 4.
```

**Solution**:
To solve this problem, we can use a two-pointer technique. We first move the right pointer `n` steps ahead, and then move both the left and right pointers together until the right pointer reaches the end of the list. This way, the left pointer will be just before the nth node from the end. We then adjust the pointers to skip the nth node.

[Link to code](019_remove_node_from_end.py)

**Notes**:
- Time complexity: O(L), where L is the length of the linked list.
- Space complexity: O(1), as we are using only a few extra pointers.

## 82. Remove Duplicates from Sorted List II

**Description**:
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

**Example**:
```plaintext
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Explanation: Given linked list: 1->2->3->3->4->4->5, remove all nodes that have duplicate numbers (3 and 4), leaving 1->2->5.
```

**Solution**:
To solve this problem, we use a dummy node to handle edge cases where the head itself might be a duplicate. We maintain two pointers: `prev` to track the node before the sequence of duplicates and `head` to traverse the list. When we find duplicates, we skip all nodes with the same value and link the previous node to the node after the last duplicate. Otherwise, we just move the `prev` pointer forward.

[Link to code](082_remove_duplicates_2.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the linked list.
- Space complexity: O(1), as the list is modified in place using only a few extra pointers.
