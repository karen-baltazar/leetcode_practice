# Problems

## 200. Number of Islands

**Description**:
Given a 2D grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example**:
```plaintext
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Solution**:
To solve this problem, we use Depth-First Search (DFS). We iterate through each cell in the grid. If the cell contains '1' and hasn't been visited yet, it is the start of a new island. We then perform DFS to mark all connected land cells as visited. Each time we start a new DFS, we increment our island count.

[Link to code](200_number_of_islands.py)

**Notes**:
- Time complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid.
- Space complexity: O(m * n), due to the space used by the visited set and the recursion stack in the worst case.

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

[Link to code](130_surrounded_regions.py)

**Notes**:
- Time complexity: O(m * n), where m is the number of rows and n is the number of columns.
- Space complexity: O(m * n), due to the recursion stack in the worst case.

## 133. Clone Graph

**Description**:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

**Example**:
```plaintext
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

Explanation:
Node 1's value is 1, and its neighbors are nodes 2 and 4.
Node 2's value is 2, and its neighbors are nodes 1 and 3.
Node 3's value is 3, and its neighbors are nodes 2 and 4.
Node 4's value is 4, and its neighbors are nodes 1 and 3.
```

**Solution**:
To solve this problem, we use Depth-First Search (DFS) with a dictionary to map each original node to its copy. This ensures that each node is copied only once, and the same copy is used whenever the node is encountered again.

[Link to code](133_clone_graph.py)

**Notes**:
- Time complexity: O(N + M), where N is the number of nodes and M is the number of edges in the graph.
- Space complexity: O(N), due to the space required for the dictionary and the recursion stack.

