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
