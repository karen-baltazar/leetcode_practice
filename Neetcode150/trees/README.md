# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| 199 | [Binary Tree Right Side View](#199-binary-tree-right-side-view) | [Explanation](#199-binary-tree-right-side-view)      | [Python Code](./199_right_side_view.py)    |
| 1448 | [Count Good Nodes in Binary Tree](#1448-count-good-nodes-in-binary-tree) | [Explanation](#1448-count-good-nodes-in-binary-tree) | [Python Code](./1448_good_nodes_bst.py)    |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal](#105-construct-binary-tree-from-preorder-and-inorder-traversal) | [Explanation](#105-construct-binary-tree-from-preorder-and-inorder-traversal) | [Python Code](./105_construct_tree.py)     |
| 124 | [Binary Tree Maximum Path Sum](#124-binary-tree-maximum-path-sum) | [Explanation](#124-binary-tree-maximum-path-sum) | [Python Code](./124_max_path_sum.py)       |
| 297 | [Serialize and Deserialize Binary Tree](#297-serialize-and-deserialize-binary-tree) | [Explanation](#297-serialize-and-deserialize-binary-tree) | [Python Code](./297_serialize_deserialize_tree.py) |

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