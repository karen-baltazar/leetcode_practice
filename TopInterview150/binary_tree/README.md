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

## 226. Invert Binary Tree

**Description**:
Given the root of a binary tree, invert the tree, and return its root.

**Example**:
```plaintext
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]
```

**Solution**:
To solve this problem, we can use either a recursive or iterative approach.

In the recursive approach, we swap the left and right children of each node and then recursively invert the left and right subtrees.

The iterative approach uses a stack to traverse the tree. For each node, we swap its left and right children and then push the children onto the stack to process them.

[Link to code](226_invert_tree.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the binary tree. This is because we visit each node exactly once.
- Space complexity: O(h) for the recursive approach due to the recursion stack, and O(n) for the iterative approach due to the stack used for traversal.

## 101. Symmetric Tree

**Description**:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

**Example**:
```plaintext
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
```

**Solution**:
To solve this problem, we use a helper function `isMirror` to recursively compare the left and right subtrees of the tree. The tree is symmetric if:
- Both subtrees are null.
- Both subtrees are not null and their root values are equal.
- The left subtree of the first tree is a mirror image of the right subtree of the second tree, and vice versa.

[Link to code](101_symmetric_tree.py)

**Notes**:
- Time complexity: O(n), where n is the number of nodes in the tree. We visit each node exactly once.
- Space complexity: O(h), where h is the height of the tree, due to the recursion stack.

## 105. Construct Binary Tree from Inorder and Preorder Traversal

**Description**:
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

**Example**:
```plaintext
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Solution**:
To solve this problem, we utilize the properties of preorder and inorder traversals:
- The first element of the preorder traversal is the root of the tree.
- The inorder traversal splits the tree into left and right subtrees.

Steps:
1. The first element of `preorder` is the root of the tree.
2. Find the index of the root in `inorder` to determine the left and right subtrees.
3. Recursively construct the left subtree using the elements before the root in `inorder` and the corresponding elements in `preorder`.
4. Recursively construct the right subtree using the elements after the root in `inorder` and the corresponding elements in `preorder`.

[Link to code](105_construct_preorder_inorder.py)

**Notes**:
- Time complexity: O(n^2) in the worst case due to the slicing of lists and index searches. 
- Space complexity: O(n), where n is the number of nodes in the tree, due to the recursion stack and the tree structure.

## 106. Construct Binary Tree from Inorder and Postorder Traversal

**Description**:
Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return the binary tree.

**Example**:
```plaintext
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
```

**Solution**:
To solve this problem, we use the properties of inorder and postorder traversals:
- The last element of the postorder traversal is the root of the tree.
- The inorder traversal splits the tree into left and right subtrees.

Steps:
1. The last element of `postorder` is the root of the tree.
2. Find the index of the root in `inorder` to determine the left and right subtrees.
3. Recursively construct the left subtree using the elements before the root in `inorder` and the corresponding elements in `postorder`.
4. Recursively construct the right subtree using the elements after the root in `inorder` and the corresponding elements in `postorder`.

[Link to code](106_construct_inorder_postorder.py)

**Notes**:
- Time complexity: O(n^2) due to list slicing.
- Space complexity: O(n), due to the recursion stack and the space required for the tree nodes.