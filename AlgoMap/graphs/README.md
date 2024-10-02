| Problem Number | Problem Name | Explanation | Code |
|----------------|-------------------------|-------------------------------------|-----------------------------|
| 1971 | [Find if Path Exists in Graph](#1971-find-if-path-exists-in-graph) | [Explanation](#1971-find-if-path-exists-in-graph) | [Python Code](./1971_valid_path.py)       |
| 200  | [Number of Islands](#200-number-of-islands) | [Explanation](#200-number-of-islands) | [Python Code](./200_num_islands.py) |
| 695  | [Max Area of Island](#695-max-area-of-island) | [Explanation](#695-max-area-of-island) | [Python Code](./695_max_area_of_island.py)|
| 207  | [Course Schedule](#207-course-schedule) | [Explanation](#207-course-schedule) | [Python Code](./207_course_schedule.py)|

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