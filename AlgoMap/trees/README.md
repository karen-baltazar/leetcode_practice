# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|--------------|-------------|------|
| 226 | [Invert Binary Tree](#226-invert-binary-tree) | [Explanation](#226-invert-binary-tree) | [Python Code](./226_invert_binary_tree.py) |

## 226. Invert Binary Tree

**Description**:
Given the root of a binary tree, invert the tree, meaning swap the left and right children for every node.

**Example**:
```plaintext
Input:
    4
   / \
  2   7
 / \ / \
1  3 6  9

Output:
    4
   / \
  7   2
 / \ / \
9  6 3  1
```

**Solution**:
This problem is solved using a recursive approach. The left and right children of each node are swapped, and the same process is applied recursively to the children. The base case is when a node is `None`, in which case the function returns `None`.

[Link to code](226_invert_binary_tree.py)

**Notes**:
- Time complexity: O(n), where `n` is the number of nodes in the tree. Each node is visited once during the recursion.
- Space complexity: O(h), where `h` is the height of the tree, due to the recursive call stack. In the worst case (a skewed tree), the space complexity could be O(n).