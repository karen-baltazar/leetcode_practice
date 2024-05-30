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

## 399. Evaluate Division

**Description**:
You are given equations in the format `A / B = k`, where `A` and `B` are variables represented as strings, and `k` is a real number (floating point). Given some queries, return the answers. If the answer does not exist, return `-1.0`.

**Example**:
```plaintext
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.0,0.5,-1.0,1.0,-1.0]

Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
```

**Solution**:
To solve this problem, we model the equations as a graph where each variable is a node, and each equation provides a directed edge with a weight corresponding to the division result. We then use Breadth-First Search (BFS) to find the value of each query by traversing the graph.

**Detailed Explanation**:

1. **Graph Representation**:
   - We represent the equations as a graph using an adjacency list.
   - Each variable in the equations is a node.
   - Each equation `A / B = k` is represented as a directed edge from `A` to `B` with weight `k`, and from `B` to `A` with weight `1/k`.

2. **Building the Graph**:
   - We use a defaultdict of lists to store the adjacency list.
   - For each equation, we add both directed edges (`A -> B` and `B -> A`) to the graph.

3. **Breadth-First Search (BFS)**:
   - We use BFS to find the path from the source variable to the target variable.
   - BFS is chosen because it ensures that we find the shortest path in an unweighted graph, which is important for minimizing the number of multiplications/divisions.
   - We initialize the BFS with a queue containing the source node and a cumulative product of `1.0`.
   - We use a set to keep track of visited nodes to avoid cycles.
   - For each node, we traverse its neighbors, updating the cumulative product, and add unvisited neighbors to the queue.
   - If we reach the target node, we return the current cumulative product.
   - If we exhaust the queue without finding the target node, we return `-1.0`.

4. **Handling Edge Cases**:
   - If either the source or target node in a query does not exist in the graph, we return `-1.0`.

[Link to code](399_evaluate_division.py)

**Notes**:
- Time complexity: O(N + Q), where N is the number of equations and Q is the number of queries.
- Space complexity: O(N), for the adjacency list and the queue used in BFS.

## 207. Course Schedule

**Description**:
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses-1`. Some courses may have prerequisites, where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` before course `ai`. Given the total number of courses and a list of prerequisite pairs, return `true` if you can finish all courses. Otherwise, return `false`.

**Example**:
```plaintext
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
```

**Solution**:
To solve this problem, we use Depth-First Search (DFS) to detect cycles in the graph. We represent the courses and their prerequisites as a directed graph using an adjacency list, where each course points to its prerequisites. We then iterate through each course, using a recursive DFS function to check for cycles. During the DFS, we maintain a set to track the nodes currently in the recursion stack, which helps in detecting cycles. If a course is already in this set, it means we've encountered a cycle, so we return False. If a course has no prerequisites or all its prerequisites can be completed without cycles, we mark it as such and return True. This ensures that each course and its dependencies are checked efficiently. If all courses can be processed without detecting any cycles, we return True, indicating that it is possible to finish all courses.

**Detailed Explanation**:

1. **Graph Representation**:
   - We represent the courses and their prerequisites as a directed graph.
   - Each course is a node, and a prerequisite relationship `A -> B` indicates that course `A` depends on course `B`.

2. **Building the Graph**:
   - We use a dictionary to store the list of prerequisites for each course.
   - For each course, we populate the dictionary with its corresponding prerequisites.

3. **Depth-First Search (DFS)**:
   - We use DFS to detect cycles in the graph.
   - A cycle indicates that it's impossible to complete the courses due to circular dependencies.
   - We maintain a set, `visitSet`, to track the nodes (courses) currently in the DFS path. This helps in detecting cycles.
   - If a course is already in `visitSet`, it means we've encountered a cycle, so we return `False`.
   - If a course has no prerequisites (`preMap[crs] == []`), it means it can be completed, so we return `True`.

4. **Processing Each Course**:
   - For each course, we initiate a DFS.
   - If any course leads to a cycle detection during its DFS, we return `False` indicating that it's not possible to complete all courses.
   - If all courses are processed without detecting any cycles, we return `True`.

5. **Handling Edge Cases**:
   - If there are no prerequisites, it means all courses can be completed, so we directly return `True`.
   - If there are isolated courses with no dependencies, they can be completed independently.

[Link to code](207_course_selection.py)

**Notes**:
- Time complexity: O(V + E), where V is the number of courses and E is the number of prerequisite pairs.
- Space complexity: O(V + E), due to the adjacency list and the recursion stack in the worst case.

## 210. Course Schedule II

**Description**:
There are a total of `numCourses` courses you have to take, labeled from 0 to `numCourses-1`. Some courses may have prerequisites, where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` before course `ai`. Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses. If there are multiple valid orderings, return any of them. If it is impossible to finish all courses, return an empty array.

**Example**:
```plaintext
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finish course 0. So a valid course order is [0,1,2,3]. Another valid order is [0,2,1,3].
```

**Solution**:
To solve this problem, we use Depth-First Search (DFS) to detect cycles in the graph and find the topological order of courses. We represent the courses and their prerequisites as a directed graph using an adjacency list. We then iterate through each course, using a recursive DFS function to check for cycles and build the topological order. During the DFS, we maintain two sets: one to track the nodes currently in the recursion stack (to detect cycles) and another to track the nodes that have been visited. If a cycle is detected, we return an empty list. If all courses can be processed without detecting any cycles, we return the topological order.

**Detailed Explanation**:

1. **Graph Representation**:
   - We represent the courses and their prerequisites as a directed graph.
   - Each course is a node, and a prerequisite relationship `A -> B` indicates that course `A` depends on course `B`.

2. **Building the Graph**:
   - We use a dictionary to store the list of prerequisites for each course.
   - For each course, we populate the dictionary with its corresponding prerequisites.

3. **Depth-First Search (DFS)**:
   - We use DFS to detect cycles and to build the topological order of courses.
   - A cycle indicates that it's impossible to complete the courses due to circular dependencies.
   - We maintain two sets: one (`cycle`) to track nodes in the current DFS path to detect cycles, and another (`visit`) to track nodes that have been fully processed.

4. **Processing Each Course**:
   - For each course, we initiate a DFS.
   - If any course leads to a cycle detection during its DFS, we return an empty list indicating that it's not possible to complete all courses.
   - If a course has no remaining prerequisites or all its prerequisites can be completed without cycles, we add it to the result list (`output`).

5. **Handling Edge Cases**:
   - If there are no prerequisites, all courses can be completed in any order, so we directly return the list of courses.
   - If there are isolated courses with no dependencies, they can be completed independently.

[Link to code](210_course_schedule_2.py)

**Notes**:
- Time complexity: O(V + E), where V is the number of courses and E is the number of prerequisite pairs.
- Space complexity: O(V + E), due to the adjacency list and the recursion stack in the worst case.
