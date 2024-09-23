# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|------------------------------------------------|------------------------------------------------------|--------------------------------------------|
| 199 | [Binary Tree Right Side View](#199-binary-tree-right-side-view) | [Explanation](#199-binary-tree-right-side-view)      | [Python Code](./199_right_side_view.py)    |

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