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
