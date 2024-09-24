# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| 199 | [Binary Tree Right Side View](#199-binary-tree-right-side-view) | [Explanation](#199-binary-tree-right-side-view)      | [Python Code](./199_right_side_view.py)    |
| 1448 | [Count Good Nodes in Binary Tree](#1448-count-good-nodes-in-binary-tree) | [Explanation](#1448-count-good-nodes-in-binary-tree) | [Python Code](./1448_good_nodes_bst.py)    |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal](#105-construct-binary-tree-from-preorder-and-inorder-traversal) | [Explanation](#105-construct-binary-tree-from-preorder-and-inorder-traversal) | [Python Code](./105_construct_tree.py)     |
| 124 | [Binary Tree Maximum Path Sum](#124-binary-tree-maximum-path-sum) | [Explanation](#124-binary-tree-maximum-path-sum) | [Python Code](./124_max_path_sum.py)       |
| 297 | [Serialize and Deserialize Binary Tree](#297-serialize-and-deserialize-binary-tree) | [Explanation](#297-serialize-and-deserialize-binary-tree) | [Python Code](./297_serialize_deserialize_tree.py) |
| 226 | [Invert Binary Tree](#226-invert-binary-tree) | [Explanation](#226-invert-binary-tree) | [Python Code](./226_invert_binary_tree.py) |
| 104 | [Maximum Depth of Binary Tree](#104-maximum-depth-of-binary-tree) | [Explanation](#104-maximum-depth-of-binary-tree) | [Python Code](./104_max_depth_bin_tree.py) |
| 110 | [Balanced Binary Tree](#110-balanced-binary-tree) | [Explanation](#110-balanced-binary-tree) | [Python Code](./110_bal_bin_tree.py) |
| 543 | [Diameter of Binary Tree](#543-diameter-of-binary-tree) | [Explanation](#543-diameter-of-binary-tree) | [Python Code](./543_diameter_bin_tree.py) |
| 100 | [Same Tree](#100-same-tree) | [Explanation](#100-same-tree) | [Python Code](./100_same_tree.py) |
| 572 | [Subtree of Another Tree](#572-subtree-of-another-tree) | [Explanation](#572-subtree-of-another-tree) | [Python Code](./572_subtree.py) |
| 102 | [Binary Tree Level Order Traversal](#102-binary-tree-level-order-traversal) | [Explanation](#102-binary-tree-level-order-traversal) | [Python Code](./102_level_order.py) |
| 230 | [Kth Smallest Element in a BST](#230-kth-smallest-element-in-a-bst) | [Explanation](#230-kth-smallest-element-in-a-bst) | [Python Code](./230_kth_smallest.py) |
| 98 | [Validate Binary Search Tree](#98-validate-binary-search-tree) | [Explanation](#98-validate-binary-search-tree)       | [Python Code](./098_validate_bst.py)        |
| 235 | [Lowest Common Ancestor of a Binary Search Tree](#235-lowest-common-ancestor-of-a-binary-search-tree) | [Explanation](#235-lowest-common-ancestor-of-a-binary-search-tree) | [Python Code](./235_lca_bst.py) |

## 199. Binary Tree Right Side View

**Description**:
Given the `root` of a binary tree, return a list of values of the nodes that are visible from the right side of the tree. The right side view of a binary tree is defined as the set of nodes you can see when looking at the tree from the right side.

**Example**:
```plaintext
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:
    1            <---
   / \
  2   3         <---
   \   \
    5   4       <---
```

**Solution**:
The solution performs a level-order traversal (BFS) of the tree, keeping track of the rightmost node at each level. For each level, the rightmost node is added to the result. The queue helps in performing the traversal, ensuring that we visit nodes level by level, from left to right, and then capture the rightmost node of each level.

[Link to code](./199_right_side_view.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the tree.
- Space complexity: O(n), due to the space used by the queue during level-order traversal.

## 1448. Count Good Nodes in Binary Tree

**Description**:
Given the root of a binary tree, count the number of "good" nodes. A node is considered "good" if, along the path from the root to the node, there is no node with a greater value than the current node.

**Example**:
```plaintext
Input: [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes 3, 3, 4, and 5 are good.
```

**Solution**:
The problem can be solved using a Depth-First Search (DFS) traversal of the tree. During the traversal, keep track of the maximum value encountered so far along the path. If the current node’s value is greater than or equal to this maximum, it is considered a "good" node. For each node, we recursively explore the left and right subtrees, updating the maximum value.

[Link to code](./1448_good_nodes_bst.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the tree, as we need to visit each node once.
- Space complexity: O(h), where h is the height of the tree, due to the recursion stack.

## 105. Construct Binary Tree from Preorder and Inorder Traversal

**Description**:
Given two integer arrays `preorder` and `inorder` representing the preorder and inorder traversal of a binary tree, construct and return the binary tree.

**Example**:
```plaintext
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Explanation: The binary tree corresponding to these traversals is:
    3
   / \
  9  20
     /  \
    15   7
```

**Solution**:
The root of the binary tree is always the first element in the `preorder` array. Using this root value, find its index in the `inorder` array, which divides the tree into left and right subtrees. Recursively apply this process for both the left and right subtrees.

[Link to code](./105_construct_tree.py)

**Notes**:
- Time complexity: O(n^2) in the worst case due to the slicing and index search in each recursive step.
- Space complexity: O(n) due to the space required by the recursive call stack.

## 124. Binary Tree Maximum Path Sum

**Description**:
Given a non-empty binary tree, return the maximum path sum. A path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

**Example**:
```plaintext
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The maximum path sum is 15 + 20 + 7 = 42.
```

**Solution**:
The solution uses a Depth-First Search (DFS) approach. At each node, the algorithm calculates the maximum path sum for both left and right subtrees, ignoring negative values. It then updates the global maximum sum if the current node can form a larger path including both subtrees. The result is the maximum sum for any path in the tree.

[Link to code](./124_max_path_sum.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the tree.
- Space complexity: O(n) due to the recursion stack.

## 297. Serialize and Deserialize Binary Tree

**Description**:
Serialization is the process of converting a data structure or object into a sequence of bits to store in a file or memory, or transmit across a network. The inverse process is called deserialization. Implement a function to serialize a binary tree to a string and another function to deserialize this string back to the original binary tree.

**Example**:
```plaintext
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Explanation: The binary tree is serialized to "1,2,N,N,3,4,N,N,5,N,N", and deserialized back to the same tree.
```

**Solution**:
- The `serialize` function uses DFS to convert the tree to a string, where 'N' represents null nodes.
- The `deserialize` function splits the serialized string and recursively reconstructs the tree using DFS, keeping track of the current index of the serialized data.

[Link to code](./297_serialize_deserialize_tree.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the tree.
- Space complexity: O(n), due to the recursion stack and storage for the serialized data.

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

## 572. Subtree of Another Tree

**Description**:
Given the roots of two binary trees, `root` and `subRoot`, determine if `subRoot` is a subtree of `root`. A subtree is a tree that consists of a node and all its descendants.

**Example**:
```plaintext
Input:
    root:    3              subRoot:  4
           / \                     / \
          4   5                   1   2
         / \
        1   2

Output:
True
```

**Solution**:
The solution involves checking if any node in the main tree is identical to the `subRoot`. This is done using a helper function `is_identical` that recursively checks if two trees are the same. The main function checks if `subRoot` is identical to the current node's subtree and recursively checks the left and right subtrees of `root` to find a match.

[Link to code](572_subtree.py)

**Notes**:
- Time complexity: O(n * m), where `n` is the number of nodes in the main tree and `m` is the number of nodes in `subRoot`. Each node in the main tree is compared to the root of `subRoot`.
- Space complexity: O(h1 + h2), where `h1` and `h2` are the heights of the main tree and `subRoot`, respectively, due to the recursive call stack.

## 102. Binary Tree Level Order Traversal

**Description**:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

**Example**:
```plaintext
Input:
    3
   / \
  9  20
    /  \
   15   7

Output:
[
  [3],
  [9,20],
  [15,7]
]
```

**Solution**:
This problem can be solved using a breadth-first search (BFS) approach with a queue. Starting from the root, the nodes are processed level by level. For each level, all nodes are dequeued, their values are recorded, and their children are enqueued for the next level. This process continues until all levels have been traversed.

[Link to code](102_level_order.py)

**Notes**:
- Time complexity: O(n), where `n` is the number of nodes in the tree. Each node is visited once.
- Space complexity: O(n), accounting for the queue, which may hold up to the entire width of the tree at the deepest level.

## 230. Kth Smallest Element in a BST

**Description**:
Given the root of a binary search tree (BST) and an integer `k`, return the `k`th smallest element in the tree.

**Example**:
```plaintext
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

**Solution**:
This problem is solved using an in-order depth-first search (DFS) traversal. The in-order traversal of a BST visits nodes in ascending order, making it ideal for finding the `k`th smallest element. As we traverse the tree, we decrement a counter starting from `k` until it reaches 0, at which point we have found the `k`th smallest element.

### Detailed Explanation:

- **Depth-First Search (DFS)**: DFS is a technique used to explore a tree or graph structure. It starts from the root and explores as far as possible along each branch before backtracking. In this problem, DFS is used to perform an in-order traversal (left -> root -> right) of the BST.
  
- **In-order Traversal**: Since the in-order traversal of a BST yields nodes in sorted order, we can simply traverse the tree, counting nodes as we go. When our count matches `k`, the current node's value is the `k`th smallest.

- **Implementation**:
  - We initialize `count` with the value of `k`, and as we traverse the tree, we decrement `count`.
  - When `count` reaches 0, we've encountered the `k`th smallest element, and we store it in `result`.
  - The recursion ensures that the traversal happens in the correct order, visiting all nodes from the smallest to the largest.

[Link to code](230_kth_smallest.py)

**Notes**:
- Time complexity: O(h + k), where `h` is the height of the tree and `k` is the number of nodes we need to visit to find the `k`th smallest element.
- Space complexity: O(h), due to the recursive call stack, where `h` is the height of the tree.

## 98. Validate Binary Search Tree

**Description**:  
Given the `root` of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example**:
```plaintext
Input: root = [2, 1, 3]
Output: true

Input: root = [5, 1, 4, null, null, 3, 6]
Output: false
```

**Solution**:  
To validate whether a tree is a binary search tree, the solution uses a recursive helper function to ensure that each node's value is within a valid range. Initially, the range is `(-∞, ∞)`, but as we move down the tree, the range is adjusted according to the value of the current node. The left subtree must have values smaller than the current node, and the right subtree must have values larger.

[Link to code](./098_validate_bst.py)

**Notes**:  
- Time complexity: O(n), where n is the number of nodes in the tree, since we visit each node exactly once.
- Space complexity: O(h), where h is the height of the tree, due to the recursion stack.

## 235. Lowest Common Ancestor of a Binary Search Tree

**Description**:  
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes `p` and `q`. The LCA is defined as the lowest node in the tree that has both `p` and `q` as descendants (where a node can be a descendant of itself).

**Example**:
```plaintext
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
```

**Solution**:  
The solution leverages the properties of a BST. For a given node:
- If both `p` and `q` are smaller, search in the left subtree.
- If both `p` and `q` are larger, search in the right subtree.
- If one node is smaller and the other larger, the current node is the lowest common ancestor.

[Link to code](./235_lca_bst.py)

**Notes**:  
- Time complexity: O(h), where h is the height of the tree.
- Space complexity: O(h), due to the recursive call stack.
