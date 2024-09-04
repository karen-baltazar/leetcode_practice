# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|--------------|-------------|------|
| 226 | [Invert Binary Tree](#226-invert-binary-tree) | [Explanation](#226-invert-binary-tree) | [Python Code](./226_invert_binary_tree.py) |
| 104 | [Maximum Depth of Binary Tree](#104-maximum-depth-of-binary-tree) | [Explanation](#104-maximum-depth-of-binary-tree) | [Python Code](./104_max_depth_bin_tree.py) |
| 110 | [Balanced Binary Tree](#110-balanced-binary-tree) | [Explanation](#110-balanced-binary-tree) | [Python Code](./110_bal_bin_tree.py) |

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

## 104. Maximum Depth of Binary Tree

**Description**:
Given the root of a binary tree, find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example**:
```plaintext
Input:
     3
    / \
   9  20
     /  \
    15   7

Output:
3
```

**Solution**:
This problem is solved using a recursive approach. The depth is determined by finding the maximum depth between the left and right subtrees, adding one for the current node. The base case is when the node is `None`, indicating that the depth is `0`.

[Link to code](104_max_depth_bin_tree.py)

**Notes**:
- Time complexity: O(n), where `n` is the number of nodes in the tree. Each node is visited once.
- Space complexity: O(h), where `h` is the height of the tree, due to the recursive call stack. In the worst case (a skewed tree), the space complexity could be O(n).

## 110. Balanced Binary Tree

**Description**:
Given a binary tree, determine if it is height-balanced. A binary tree is considered balanced if the depths of the two subtrees of every node never differ by more than one.

**Example**:
```plaintext
Input:
    3
   / \
  9  20
    /  \
   15   7

Output:
True
```

**Solution**:
The solution uses a recursive function to calculate the height of each subtree and checks the balance condition at each node. The function returns early if it detects that the tree is unbalanced. A list is used to track the balance status across recursive calls.

[Link to code](110_bal_bin_tree.py)

**Notes**:
- Time complexity: O(n), where `n` is the number of nodes in the tree. Each node is visited once.
- Space complexity: O(h), where `h` is the height of the tree, due to the recursive call stack. In the worst case (a skewed tree), the space complexity could be O(n).