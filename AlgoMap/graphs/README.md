# Problems

| Problem Number | Problem Name | Explanation | Code |
|----------------|-------------------------|-------------------------------------|-----------------------------|
| 1971 | [Find if Path Exists in Graph](#1971-find-if-path-exists-in-graph) | [Explanation](#1971-find-if-path-exists-in-graph) | [Python Code](./1971_valid_path.py)       |
| 200  | [Number of Islands](#200-number-of-islands) | [Explanation](#200-number-of-islands) | [Python Code](./200_num_islands.py) |
| 695  | [Max Area of Island](#695-max-area-of-island) | [Explanation](#695-max-area-of-island) | [Python Code](./695_max_area_of_island.py)|
| 207  | [Course Schedule](#207-course-schedule) | [Explanation](#207-course-schedule) | [Python Code](./207_course_schedule.py)|
| 210  | [Course Schedule II](#210-course-schedule-ii) | [Explanation](#210-course-schedule-ii) | [Python Code](./210_course_schedule_ii.py)|
| 417  | [Pacific Atlantic Water Flow](#417-pacific-atlantic-water-flow) | [Explanation](#417-pacific-atlantic-water-flow)     | [Python Code](./417_pacific_atlantic.py)   |
| 133  | [Clone Graph](#133-clone-graph) | [Explanation](#133-clone-graph) | [Python Code](./133_clone_graph.py)       |
| 994  | [Rotting Oranges](#994-rotting-oranges) | [Explanation](#994-rotting-oranges) | [Python Code](./994_rotting_oranges.py)   |
| 1584 | [Min Cost to Connect All Points](#1584-min-cost-to-connect-all-points) | [Explanation](#1584-min-cost-to-connect-all-points) | [Python Code](./1584_min_cost_connect_points.py) |

## 1971. Find if Path Exists in Graph

**Description**:
Given an undirected graph represented as `n` nodes and a list of edges, determine if there is a valid path between two given nodes, `src` and `dst`.

**Example**:
```plaintext
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: False
Explanation: There is no path from node 0 to node 5.
```

**Solution**:
This problem is solved using Depth-First Search (DFS):
- Build the graph using an adjacency list.
- Traverse the graph starting from the source node using DFS.
- Check if the destination node can be reached during the DFS traversal.

[Link to code](./1971_valid_path.py)

**Notes**:
- Time complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges. This is because we visit each node and edge once.
- Space complexity: O(V), due to the space needed for the adjacency list and the visited set.

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

## 1584. Min Cost to Connect All Points

**Description**:
You are given `n` points in a 2D plane where `points[i] = [x_i, y_i]` represents the coordinates of the i-th point. The task is to connect all the points with the minimum cost, where the cost of connecting two points is the **Manhattan distance** between them:  
`distance = |x1 - x2| + |y1 - y2|`.  
Return the minimum cost required to make all points connected. All points must be connected directly or indirectly.

**Example**:
```plaintext
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
```

**Solution**:
This problem can be solved efficiently using **Prim's Algorithm** to build a **Minimum Spanning Tree (MST)**. The idea is to start with an arbitrary point and grow the MST by always adding the closest (cheapest) unvisited point. The edge weights between points are determined by the Manhattan distance, making this a variation of the MST problem in 2D space.

**Approach**:
1. **Initialization**: Start by selecting an arbitrary point, usually the first one. Push it into a min-heap (priority queue) with an initial cost of 0 because the cost to connect the first point is zero.
2. **Visit Nodes**: At each step, pick the point with the smallest cost from the heap. Mark this point as visited, which means it is now part of the MST.
3. **Update Costs**: For the current point, calculate the Manhattan distance to all unvisited points. For each unvisited point, if the calculated cost to connect it is smaller than any previously recorded cost, update the heap with this new cost.
4. **Repeat**: Repeat this process until all points are visited and connected.
5. **Result**: The sum of the edge weights (distances) added to the MST will be the minimum cost to connect all points.

[Link to code](./1584_min_cost_connect_points.py)

**Notes**:
- Time complexity: O(N² log N), where `N` is the number of points. This arises from calculating the Manhattan distances between all pairs of points (O(N²)) and managing the priority queue (heap) for edge selection (O(log N)).
- Space complexity: O(N), due to the storage of the heap and visited set.