# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|--------------|-------------|------|
| 226 | [Invert Binary Tree](#226-invert-binary-tree) | [Explanation](#226-invert-binary-tree) | [Python Code](./226_invert_binary_tree.py) |
| 104 | [Maximum Depth of Binary Tree](#104-maximum-depth-of-binary-tree) | [Explanation](#104-maximum-depth-of-binary-tree) | [Python Code](./104_max_depth_bin_tree.py) |
| 110 | [Balanced Binary Tree](#110-balanced-binary-tree) | [Explanation](#110-balanced-binary-tree) | [Python Code](./110_bal_bin_tree.py) |
| 543 | [Diameter of Binary Tree](#543-diameter-of-binary-tree) | [Explanation](#543-diameter-of-binary-tree) | [Python Code](./543_diameter_bin_tree.py) |
| 100 | [Same Tree](#100-same-tree) | [Explanation](#100-same-tree) | [Python Code](./100_same_tree.py) |
| 101 | [Symmetric Tree](#101-symmetric-tree) | [Explanation](#101-symmetric-tree) | [Python Code](./101_symmetric_tree.py) |
| 112 | [Path Sum](#112-path-sum) | [Explanation](#112-path-sum) | [Python Code](./112_path_sum.py) |
| 572 | [Subtree of Another Tree](#572-subtree-of-another-tree) | [Explanation](#572-subtree-of-another-tree) | [Python Code](./572_subtree.py) |
| 102 | [Binary Tree Level Order Traversal](#102-binary-tree-level-order-traversal) | [Explanation](#102-binary-tree-level-order-traversal) | [Python Code](./102_level_order.py) |
| 230 | [Kth Smallest Element in a BST](#230-kth-smallest-element-in-a-bst) | [Explanation](#230-kth-smallest-element-in-a-bst) | [Python Code](./230_kth_smallest.py) |
| 530 | [Minimum Absolute Difference in BST](#530-minimum-absolute-difference-in-bst) | [Explanation](#530-minimum-absolute-difference-in-bst) | [Python Code](./530_min_abs_diff_bst.py)  |
| 98 | [Validate Binary Search Tree](#98-validate-binary-search-tree) | [Explanation](#98-validate-binary-search-tree)       | [Python Code](./098_validate_bst.py)        |
| 235 | [Lowest Common Ancestor of a Binary Search Tree](#235-lowest-common-ancestor-of-a-binary-search-tree) | [Explanation](#235-lowest-common-ancestor-of-a-binary-search-tree) | [Python Code](./235_lca_bst.py) |
| 208 | [Implement Trie (Prefix Tree)](#208-implement-trie-prefix-tree) | [Explanation](#208-implement-trie-prefix-tree)       | [Python Code](./208_implement_trie.py)     |

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

## 101. Symmetric Tree

**Description**:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

**Example**:
```plaintext
Input:
    1
   / \
  2   2
 / \ / \
3  4 4  3

Output:
True
```

**Solution**:
The solution involves comparing the left and right subtrees of the tree. For the tree to be symmetric, the left subtree of the left child must be a mirror image of the right subtree of the right child, and vice versa. This comparison is done recursively. The base case checks if both nodes are `None`, in which case they are symmetric. If one is `None` or their values do not match, the tree is not symmetric.

[Link to code](101_symmetric_tree.py)

**Notes**:
- Time complexity: O(n), where `n` is the number of nodes in the tree. Each node is visited once.
- Space complexity: O(h), where `h` is the height of the tree, due to the recursive call stack.

## 112. Path Sum

**Description**:
Given the root of a binary tree and a target sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the target sum.

**Example**:
```plaintext
Input:
    5
   / \
  4   8
 /   / \
11  13  4
/  \      \
7    2      1

Target Sum: 22

Output:
True
```

**Solution**:
The solution involves traversing the tree recursively to check if any root-to-leaf path sums up to the target value. If a leaf node is reached and the sum of the path from the root to this node equals the target sum, the path is valid. The function recursively checks each node and updates the current path sum. If the path sum equals the target sum at any leaf node, it returns `True`. Otherwise, it continues checking other paths.

[Link to code](112_path_sum.py)

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

## 530. Minimum Absolute Difference in BST

**Description**:  
Given a binary search tree (BST), find the minimum absolute difference between the values of any two different nodes.

**Example**:
```plaintext
Input: root = [4, 2, 6, 1, 3]
Output: 1

Input: root = [0, null, 2236, 1277, 2776, 519]
Output: 519
```

**Solution**:  
The solution uses an in-order traversal to process the nodes in sorted order. During the traversal, we compare the value of each node with the previously visited node and update the minimum difference. We store the previous node’s value and the minimum difference found so far. This ensures we get the smallest possible difference between any two nodes in the BST.

[Link to code](./530_min_abs_diff_bst.py)

**Notes**:  
- Time complexity: O(n), where n is the number of nodes in the tree, since we visit each node once.
- Space complexity: O(h), where h is the height of the tree, due to the recursion stack used during DFS.

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

## 208. Implement Trie (Prefix Tree)

**Description**:
Implement a Trie (Prefix Tree) that supports three operations:
- `insert(word)`: Inserts a word into the trie.
- `search(word)`: Returns `True` if the word is in the trie (with a valid end marker), otherwise returns `False`.
- `startsWith(prefix)`: Returns `True` if there is any word in the trie that starts with the given prefix, otherwise returns `False`.

**Example**:
```plaintext
Input:
    trie = Trie()
    trie.insert("apple")
    trie.search("apple")   # Returns True
    trie.search("app")     # Returns False
    trie.startsWith("app") # Returns True
    trie.insert("app")
    trie.search("app")     # Returns True
```

**Solution**:
The Trie is implemented as a dictionary where each character in a word leads to a new dictionary (representing the next level of the trie). Words are inserted character by character, and the end of a word is marked using a special `#` symbol. The `insert()` method adds characters to the trie as needed. The `search()` method verifies if a word exists in the trie by checking each character and looking for the end marker `#`. The `startsWith()` method checks if a given prefix exists by traversing the trie without checking for the end marker.

[Link to code](./208_implement_trie.py)

**Notes**:
- Time complexity:
  - `insert(word)`: O(n), where n is the length of the word.
  - `search(word)` and `startsWith(prefix)`: O(m), where m is the length of the word or prefix.
- Space complexity: O(n), where n is the total number of characters inserted into the trie.