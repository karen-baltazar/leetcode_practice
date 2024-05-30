class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Hint: Keep track of visited cells to avoid counting the same island multiple times.
        
        # Get the number of rows and columns in the grid
        rows = len(grid)
        cols = len(grid[0])
        # Set to keep track of visited cells
        visited = set()
        # Variable to count the number of islands
        result = 0

        # Depth-first search helper function
        def dfs(r, c):
            # If the cell is already visited, return
            if (r, c) in visited:
                return

            # Mark the cell as visited
            visited.add((r, c))
            # List of possible directions to move (down, up, right, left)
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            # Explore all possible directions
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                # If the new cell is within bounds and is land ("1"), perform DFS on it
                if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1"):
                    dfs(nr, nc)

        # Iterate over each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land ("1") and not visited, it's a new island
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    result += 1  # Increment the island count

        # Return the total number of islands
        return result
