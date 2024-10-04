# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|----------------------------------|----------------------------------|----------------------------------|
| 286  | [Walls and Gates](#286-walls-and-gates) | [Explanation](#286-walls-and-gates) | [Python Code](./286_walls_and_gates.py) |
| 130  | [Surrounded Regions](#130-surrounded-regions) | [Explanation](#130-surrounded-regions) | [Python Code](./130_surrounded_regions.py) |
| 261  | [Graph Valid Tree](#261-graph-valid-tree) | [Explanation](#261-graph-valid-tree) | [Python Code](./261_graph_valid_tree.py) |
| 323  | [Number of Connected Components](#323-number-of-connected-components) | [Explanation](#323-number-of-connected-components) | [Python Code](./323_connected_components.py) |

## 286. Walls and Gates

**Description**:
You are given a grid representing rooms in a building. A value of `-1` represents a wall or obstacle, `0` represents a gate, and `INF (2147483647)` represents an empty room. Your task is to fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, leave the room as `INF`.

**Example**:
```plaintext
Input:
[[2147483647, -1, 0, 2147483647],
 [2147483647, 2147483647, 2147483647, -1],
 [2147483647, -1, 2147483647, -1],
 [0, -1, 2147483647, 2147483647]]

Output:
[[3, -1, 0, 1],
 [2, 2, 1, -1],
 [1, -1, 2, -1],
 [0, -1, 3, 4]]
```

**Solution**:
We apply a BFS (Breadth-First Search) starting from all gates at the same time. This ensures that the shortest distance from each gate to any empty room is calculated efficiently. For each gate, we propagate its distance to neighboring rooms, and the distance increases incrementally as we move further from the gates.

At each step of the BFS, we check the neighboring rooms in four directions (up, down, left, right) and update the distance only for cells that contain `INF` (empty rooms). This guarantees that we only fill rooms that haven't been visited yet or whose shortest distance hasn't been determined.

[Link to code](./286_walls_and_gates.py)

**Notes**:
- Time complexity: O(m * n), where `m` is the number of rows and `n` is the number of columns, as each cell is processed at most once.
- Space complexity: O(m * n) for the queue used in BFS.

## 130. Surrounded Regions

**Description**:
Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions that are 4-directionally surrounded by `'X'`. A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

**Example**:
```plaintext
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and not connected to an 'O' on the border will be flipped to 'X'.
```

**Solution**:
To solve this problem, we use Depth-First Search (DFS) to mark all `'O'`s connected to the border as temporary `'T'`. These `'O'`s cannot be surrounded. After marking, we iterate over the board to flip all surrounded `'O'`s to `'X'`. Finally, we revert the temporary `'T'`s back to `'O'`.

[Link to code](./130_surrounded_regions.py)

**Notes**:
- Time complexity: O(m * n), where m is the number of rows and n is the number of columns.
- Space complexity: O(m * n), due to the recursion stack in the worst case.

## 261. Graph Valid Tree

**Description**:
Given `n` nodes labeled from `0` to `n - 1` and a list of edges where each edge connects two nodes, determine if the nodes form a valid tree. A valid tree must be:
1. **Connected**: All nodes must be reachable from any other node.
2. **Acyclic**: There should be no cycles in the graph.

**Example**:
```plaintext
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: True
```

**Solution**:
To solve this, we use Depth-First Search (DFS). The key is to traverse the graph and check for:
1. **Cycles**: If we revisit a node we've already visited (that isn't the parent node), there is a cycle.
2. **Connectivity**: After the DFS, if all nodes have been visited, the graph is connected.

We keep track of visited nodes and ensure no cycles exist using a `prev_node` to avoid revisiting the previous node from which we came.

[Link to code](./261_graph_valid_tree.py)

**Notes**:
- Time complexity: O(n + e), where `n` is the number of nodes and `e` is the number of edges.
- Space complexity: O(n + e) due to the adjacency list and DFS stack.

## 323. Number of Connected Components

**Description**:
You are given `n` nodes, labeled from `0` to `n-1`, and a list of `edges` where each edge connects two nodes. Your task is to return the number of connected components in the graph. A connected component is a subset of nodes such that there is a path between any two nodes in the subset.

**Example**:
```plaintext
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Explanation: There are two connected components: {0, 1, 2} and {3, 4}.
```

**Solution**:
We can solve this problem using the **Union-Find** (or Disjoint Set Union) algorithm. The goal is to group nodes into connected components by performing two operations:
1. **Find**: Identify which component a particular node belongs to.
2. **Union**: Connect two components if an edge exists between them.

The **Union-Find** algorithm works efficiently when optimized with:
- **Path compression**: This technique speeds up the `find` operation by making each node point directly to the root of its set during the traversal, thereby flattening the structure.
- **Union by rank**: When connecting two components, we attach the smaller component to the larger one. This keeps the tree representing the components balanced and reduces the overall height.

For each edge, we:
1. Check the components of both nodes using `find`.
2. If they belong to different components, we merge them using `union` and reduce the total number of components by 1.
3. Finally, return the total number of components left.

[Link to code](./323_connected_components.py)

**Notes**:
- Time complexity: O(n + e * α(n)), where `n` is the number of nodes, `e` is the number of edges, and `α(n)` is the inverse Ackermann function (very small, almost constant).
- Space complexity: O(n) for the parent and rank arrays.