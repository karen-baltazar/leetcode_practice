# Problems

## 104. Maximum Depth of Binary Tree

**Description**:
Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example**:
```plaintext
Input: root = [3,9,20,null,null,15,7]
Output: 3
Explanation: The longest path is 3 -> 20 -> 15 or 3 -> 20 -> 7, both have a depth of 3.
```

**Solution**:
To solve this problem, we use a recursive approach. The base case is when the node is `None`, in which case the depth is 0. For each node, we recursively compute the depth of its left and right subtrees and take the maximum of the two, adding one to account for the current node. This ensures that we always find the longest path from the root to a leaf.

[Link to code](104_max_depth.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the tree. This is because we visit each node exactly once.
- Space complexity: O(h), where h is the height of the tree. This is due to the recursion stack. In the worst case (for a completely unbalanced tree), this can be O(n).