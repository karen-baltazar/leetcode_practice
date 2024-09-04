# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|--------------|-------------|------|
| 226 | [Invert Binary Tree](#226-invert-binary-tree) | [Explanation](#226-invert-binary-tree) | [Python Code](./226_invert_binary_tree.py) |
| 104 | [Maximum Depth of Binary Tree](#104-maximum-depth-of-binary-tree) | [Explanation](#104-maximum-depth-of-binary-tree) | [Python Code](./104_max_depth_bin_tree.py) |
| 110 | [Balanced Binary Tree](#110-balanced-binary-tree) | [Explanation](#110-balanced-binary-tree) | [Python Code](./110_bal_bin_tree.py) |
| 543 | [Diameter of Binary Tree](#543-diameter-of-binary-tree) | [Explanation](#543-diameter-of-binary-tree) | [Python Code](./543_diameter_bin_tree.py) |
| 100 | [Same Tree](#100-same-tree) | [Explanation](#100-same-tree) | [Python Code](./100_same_tree.py) |

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

## 543. Diameter of Binary Tree

**Description**:
Given the root of a binary tree, return the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

**Example**:
```plaintext
Input:
    1
   / \
  2   3
 / \
4   5

Output:
3
```

**Solution**:
The solution involves calculating the height of the left and right subtrees for each node and summing these heights to get the diameter passing through that node. The largest diameter encountered during the traversal is stored and returned. The height function is used recursively to calculate both the height and the diameter at each node.

[Link to code](543_diameter_bin_tree.py)

**Notes**:
- Time complexity: O(n), where `n` is the number of nodes in the tree. Each node is visited once.
- Space complexity: O(h), where `h` is the height of the tree, due to the recursive call stack. In the worst case (a skewed tree), the space complexity could be O(n).

## 100. Same Tree

**Description**:
Given the roots of two binary trees, determine if they are the same or not. Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

**Example**:
```plaintext
Input:
    p:    1       q:    1
         / \          / \
        2   3        2   3

Output:
True
```

**Solution**:
This problem is solved using a recursive approach. The function checks if both nodes are `None`, in which case they are the same up to that point. If one node is `None` and the other is not, or their values don't match, the trees are not the same. The function then recursively checks the left and right subtrees, and both must be identical for the trees to be considered the same.

[Link to code](100_same_tree.py)

**Notes**:
- Time complexity: O(n), where `n` is the number of nodes in the tree. Each node is visited once.
- Space complexity: O(h), where `h` is the height of the tree, due to the recursive call stack.