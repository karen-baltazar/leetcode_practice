# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|----------------------------------|----------------------------------|----------------------------------|
| 286  | [Walls and Gates](#286-walls-and-gates) | [Explanation](#286-walls-and-gates) | [Python Code](./286_walls_and_gates.py) |
| 130  | [Surrounded Regions](#130-surrounded-regions) | [Explanation](#130-surrounded-regions) | [Python Code](./130_surrounded_regions.py) |

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
