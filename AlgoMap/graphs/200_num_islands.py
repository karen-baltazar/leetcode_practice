class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the number of rows and columns in the grid
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        # Set to keep track of visited cells
        visited = set()
        
        # Variable to count the number of islands
        island_count = 0

        # Helper function to perform DFS and mark connected land ('1') as visited
        def dfs(row, col):
            # If this cell has been visited, return
            if (row, col) in visited:
                return

            # Mark the current cell as visited
            visited.add((row, col))
            
            # Define directions for exploring neighbors (down, up, right, left)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            # Explore all valid neighboring cells
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the new position is within bounds and is land ('1')
                if (0 <= new_row < num_rows and 
                    0 <= new_col < num_cols and 
                    grid[new_row][new_col] == "1"):
                    # Recursively apply DFS to the neighboring land cell
                    dfs(new_row, new_col)

        # Iterate over each cell in the grid
        for row in range(num_rows):
            for col in range(num_cols):
                # If the cell is land ('1') and has not been visited, it's a new island
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)  # Perform DFS to mark the entire island
                    island_count += 1  # Increment the island count

        return island_count
