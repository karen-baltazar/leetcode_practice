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

## 100. Same Tree

**Description**:
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example**:
```plaintext
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false
```

**Solution**:
To solve this problem, we use a recursive approach. We compare the values of the current nodes of both trees. If they match, we recursively check their left and right subtrees. If both subtrees are identical, the trees are considered the same. The base case for the recursion is when both nodes are `None`, which means we have reached the end of both trees.

[Link to code](100_same_tree.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the binary trees. This is because we visit each node exactly once.
- Space complexity: O(h), where h is the height of the binary trees. This is due to the recursion stack used for depth-first traversal.