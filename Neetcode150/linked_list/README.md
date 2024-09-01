# Problems

| Problem Number | Problem Name                                   | Explanation                                          | Code                                       |
|----------------|------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| 143            | [Reorder List](#143-reorder-list)              | [Explanation](#143-reorder-list)                     | [Python Code](./143_reorder_list.py)       |

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