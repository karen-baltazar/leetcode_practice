# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|----------------------------------|----------------------------------|----------------------------------|
| 286  | [Walls and Gates](#286-walls-and-gates) | [Explanation](#286-walls-and-gates) | [Python Code](./286_walls_and_gates.py) |
| 130  | [Surrounded Regions](#130-surrounded-regions) | [Explanation](#130-surrounded-regions) | [Python Code](./130_surrounded_regions.py) |
| 261  | [Graph Valid Tree](#261-graph-valid-tree) | [Explanation](#261-graph-valid-tree) | [Python Code](./261_graph_valid_tree.py) |
| 323  | [Number of Connected Components](#323-number-of-connected-components) | [Explanation](#323-number-of-connected-components) | [Python Code](./323_connected_components.py) |
| 684  | [Redundant Connection](#684-redundant-connection) | [Explanation](#684-redundant-connection) | [Python Code](./684_redundant_connection.py)  |
| 127  | [Word Ladder](#127-word-ladder) | [Explanation](#127-word-ladder) | [Python Code](./127_word_ladder.py)       |
| 200  | [Number of Islands](#200-number-of-islands) | [Explanation](#200-number-of-islands) | [Python Code](./200_num_islands.py) |
| 695  | [Max Area of Island](#695-max-area-of-island) | [Explanation](#695-max-area-of-island) | [Python Code](./695_max_area_of_island.py)|
| 207  | [Course Schedule](#207-course-schedule) | [Explanation](#207-course-schedule) | [Python Code](./207_course_schedule.py)|
| 210  | [Course Schedule II](#210-course-schedule-ii) | [Explanation](#210-course-schedule-ii) | [Python Code](./210_course_schedule_ii.py)|
| 417  | [Pacific Atlantic Water Flow](#417-pacific-atlantic-water-flow) | [Explanation](#417-pacific-atlantic-water-flow)     | [Python Code](./417_pacific_atlantic.py)   |
| 133  | [Clone Graph](#133-clone-graph) | [Explanation](#133-clone-graph) | [Python Code](./133_clone_graph.py)       |
| 994  | [Rotting Oranges](#994-rotting-oranges) | [Explanation](#994-rotting-oranges) | [Python Code](./994_rotting_oranges.py)   |

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

## 684. Redundant Connection

**Description**:
You are given a tree (an acyclic graph) with `n` nodes where exactly one edge is added, making it into a cycle. You need to find and return that redundant edge.

The input consists of a 2D array `edges`, where each element is an edge between two nodes. The task is to identify the edge that, if removed, leaves the graph as a valid tree.

**Example**:
```plaintext
Input: edges = [[1, 2], [1, 3], [2, 3]]
Output: [2, 3]
```

**Solution**:
This problem is solved using the **Union-Find (Disjoint Set Union)** data structure to detect cycles in the graph. A cycle exists when two nodes that are already in the same connected component are connected by an edge.

The **Union-Find** algorithm operates as follows:
1. **Find**: Determine which component (or set) a node belongs to using path compression.
2. **Union**: Combine two components if they are different using union by rank to keep the tree balanced.

In the solution:
1. We initialize a `parent` array where each node is its own parent.
2. Path compression is applied to the `find` function to make future lookups faster.
3. Union by rank ensures that we attach smaller trees to larger ones.

As we process each edge, we attempt to union the two nodes it connects. If they are already connected, this edge forms a cycle and is the redundant edge we are looking for.

[Link to code](./684_redundant_connection.py)

**Notes**:
- Time complexity: O(n), where `n` is the number of edges. Both `find` and `union` operations run in almost constant time due to path compression and union by rank.
- Space complexity: O(n), due to the `parent` and `rank` arrays.

## 127. Word Ladder

**Description**:
Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
1. Only one letter can be changed at a time.
2. Each transformed word must exist in the wordList.

If no such transformation sequence exists, return `0`.

**Example**:
```plaintext
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which takes 5 steps.
```

**Solution**:
This problem can be solved using Breadth-First Search (BFS) to find the shortest path (in terms of transformations) from `beginWord` to `endWord`. Here's a breakdown of the approach:

1. **Pattern Mapping**:
   - First, we preprocess the `wordList` by creating a dictionary that maps patterns (words with one character replaced by `*`) to all words that can fit that pattern.
   - For example, for the word "hot", patterns like `*ot`, `h*t`, and `ho*` are created, and this word is mapped to each of those patterns in a dictionary. This helps in quickly finding neighboring words that differ by only one character.

2. **Breadth-First Search (BFS)**:
   - We start BFS from the `beginWord` and try to transform it to the `endWord` by exploring all possible words that can be reached by changing just one letter.
   - For each word, we generate all possible patterns and look for neighboring words (words that match those patterns) in the dictionary.
   - We use a queue to perform BFS and a set to keep track of visited words.

3. **Stopping Condition**:
   - The BFS stops when the `endWord` is found, and the number of transformations (or steps) taken is returned.
   - If the `endWord` is not found, return `0`.

[Link to code](./127_word_ladder.py)

**Notes**:
- Time Complexity: `O(N * M^2)`, where `N` is the number of words in `wordList`, and `M` is the length of the words. We iterate through each word in the list, and for each word, we create `M` patterns and search through the neighbors.
- Space Complexity: `O(N * M)`, since we store the dictionary of patterns and the queue for BFS.

## 200. Number of Islands

**Description**:
Given a 2D grid of `1`s (land) and `0`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

**Example**:
```plaintext
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
Explanation: There are three islands: 
- The first is in the upper left,
- The second is in the center,
- The third is in the lower right.
```

**Solution**:
This problem is solved using Depth-First Search (DFS):
- Iterate through the grid and perform DFS when encountering land ('1') that hasn't been visited yet.
- Each DFS marks the entire island as visited.
- The total number of DFS calls corresponds to the number of islands.

[Link to code](./200_num_islands.py)

**Notes**:
- Time complexity: O(n * m), where n is the number of rows and m is the number of columns. Every cell is visited once.
- Space complexity: O(n * m), due to the recursion stack and the `visited` set.

## 695. Max Area of Island

**Description**:
Given a 2D grid of `1`s (land) and `0`s (water), return the maximum area of an island in the grid. An island is a group of adjacent lands connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

**Example**:
```plaintext
Input: grid = [
  [0,0,1,0,0],
  [0,1,1,1,0],
  [0,0,0,1,1],
  [0,0,0,0,1]
]
Output: 4
Explanation: The largest island has an area of 4.
```

**Solution**:
This problem is solved using Depth-First Search (DFS):
- Iterate through the grid and perform DFS when encountering land ('1').
- Each DFS call calculates the area of the connected island and returns it.
- Track the maximum area encountered during the DFS calls.

[Link to code](./695_max_area_of_island.py)

**Notes**:
- Time complexity: O(n * m), where n is the number of rows and m is the number of columns. Every cell is visited once.
- Space complexity: O(n * m), due to the recursion stack for DFS.

## 207. Course Schedule

**Description**:
You are given the total number of courses (`numCourses`) you have to take, labeled from 0 to `numCourses-1`. You are also given a list of prerequisite pairs, where each pair `[a, b]` indicates that to take course `a`, you must first complete course `b`. Return `True` if it is possible to finish all courses, otherwise return `False`.

**Example**:
```plaintext
Input: numCourses = 2, prerequisites = [[1, 0]]
Output: True
Explanation: You can finish course 1 after taking course 0.
```

**Solution**:
This problem can be solved using a Depth-First Search (DFS) approach:
- We create an adjacency list that maps each course to its prerequisites using a `defaultdict`.
- We then perform DFS for each course to check if it can be completed without encountering a cycle.
- If a cycle is detected during the DFS traversal, it means that the course requirements cannot be satisfied, and we return `False`.

[Link to code](./207_course_schedule.py)

**Notes**:
- Time complexity: O(n + e), where n is the number of courses and e is the number of prerequisite pairs.
- Space complexity: O(n), due to the recursive call stack and the prerequisite map.

## 210. Course Schedule II

**Description**:
You are given the total number of courses (`numCourses`) you have to take, labeled from 0 to `numCourses-1`. You are also given a list of prerequisite pairs, where each pair `[a, b]` indicates that to take course `a`, you must first complete course `b`. Return the ordering of courses you should take to finish all courses. If there are multiple valid answers, return any of them. If it is impossible to finish all courses, return an empty list.

**Example**:
```plaintext
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3] or [0,1,2,3]
Explanation: Both are valid course orders.
```

**Solution**:
This problem is solved using DFS to detect cycles and build the course order:
- We use a `defaultdict` to map each course to its prerequisites.
- DFS is used to check for cycles (courses that are prerequisites of themselves) and to build the course order.
- If a cycle is found, it means that the courses cannot be completed, and we return an empty list.
- The result is constructed in reverse order since we append the courses after all their prerequisites have been processed.

[Link to code](./210_course_schedule_ii.py)

**Notes**:
- Time complexity: O(n + e), where n is the number of courses and e is the number of prerequisite pairs.
- Space complexity: O(n), due to the recursive call stack and the prerequisite map.

## 417. Pacific Atlantic Water Flow

**Description**:
You are given an `m x n` matrix of heights, where `heights[r][c]` represents the height of land at position `(r, c)`. Water can flow from a cell to another if the next cell is both within bounds and has an equal or lower height. The Pacific Ocean touches the left and top edges of the matrix, while the Atlantic Ocean touches the right and bottom edges. Return a list of all cells where water can flow to both the Pacific and Atlantic oceans.

**Example**:
```plaintext
Input: heights = [[1,2,2,3,5],
                  [3,2,3,4,4],
                  [2,4,5,3,1],
                  [6,7,1,4,5],
                  [5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

**Solution**:
We solve this problem using Depth-First Search (DFS):
- We start from the edges of the matrix (the cells adjacent to both oceans) and perform DFS to find all cells that can reach each ocean.
- We keep track of visited cells for both the Pacific and Atlantic oceans using two sets.
- The result is the intersection of the two sets, which contains cells that can reach both oceans.

[Link to code](./417_pacific_atlantic.py)

**Notes**:
- Time complexity: O(m * n), where `m` is the number of rows and `n` is the number of columns in the grid.
- Space complexity: O(m * n) due to the recursive call stack and the visited sets.

## 133. Clone Graph

**Description**:
You are given a reference to a node in a connected undirected graph. Each node has a value and a list of neighbors. Your task is to return a deep copy (clone) of the graph.

**Example**:
```plaintext
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: The graph has 4 nodes as follows:
1 -- 2
|    |
4 -- 3
```

**Solution**:
We can solve this problem using Depth-First Search (DFS):
- We maintain a dictionary (`old_to_new`) to map original nodes to their cloned counterparts.
- We recursively clone each node and its neighbors using DFS.
- The cloned graph is built from the given starting node.

[Link to code](./133_clone_graph.py)

**Notes**:
- Time complexity: O(N + E), where `N` is the number of nodes and `E` is the number of edges.
- Space complexity: O(N) for the recursion stack and the mapping dictionary.

## 994. Rotting Oranges

**Description**:
You are given a grid where:
- `0` represents an empty cell.
- `1` represents a fresh orange.
- `2` represents a rotten orange.
Your task is to determine the minimum number of minutes that must elapse until no fresh orange remains. If this is impossible, return `-1`.

**Example**:
```plaintext
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Explanation: The grid looks like this:
2 1 1
1 1 0
0 1 1
After 1 minute: 
2 2 1
2 1 0
0 1 1
After 2 minutes:
2 2 2
2 2 0
0 1 1
After 3 minutes:
2 2 2
2 2 0
0 2 1
After 4 minutes:
2 2 2
2 2 0
0 2 2
```

**Solution**:
This problem can be solved using a Breadth-First Search (BFS) approach:
- Add all the initially rotten oranges to a queue and process them level by level (minute by minute).
- For each rotten orange, rot its neighboring fresh oranges and reduce the count of fresh oranges.
- Continue this process until either all fresh oranges have rotted or no more fresh oranges can be rotted.

[Link to code](./994_rotting_oranges.py)

**Notes**:
- Time complexity: O(N), where `N` is the number of cells in the grid.
- Space complexity: O(N) for the queue used in BFS.