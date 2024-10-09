class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get number of rows and columns in the grid
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        # Variable to track the maximum area of an island
        max_area = 0

        # Helper function to perform DFS and calculate the area of an island
        def dfs(row, col):
            # Mark the current cell as visited by setting it to 0 (water)
            grid[row][col] = 0
            
            # Define directions for exploring neighbors (down, up, right, left)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            # Variable to track the current area of the island
            area = 0

            # Explore all valid neighboring cells
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check if the new position is within bounds and is land (1)
                if (0 <= new_row < num_rows and 
                    0 <= new_col < num_cols and 
                    grid[new_row][new_col] == 1):
                    # Recursively apply DFS to the neighboring land cell and accumulate area
                    area += dfs(new_row, new_col)

            # Return 1 (current cell) + area of neighboring cells
            return 1 + area

        # Iterate over each cell in the grid
        for row in range(num_rows):
            for col in range(num_cols):
                # If the cell is land (1), compute the area of the island using DFS
                if grid[row][col] == 1:
                    # Update the maximum area found so far
                    max_area = max(max_area, dfs(row, col))

        return max_area
