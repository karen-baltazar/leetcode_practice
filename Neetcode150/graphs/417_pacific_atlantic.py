class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific, atlantic = set(), set()

        # Helper function for DFS to explore cells and mark reachable ocean cells
        def dfs(r, c, visited):
            # If the cell is already visited, return
            if (r, c) in visited:
                return

            # Mark the current cell as visited
            visited.add((r, c))

            # Explore neighboring cells in four directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r + dr, c + dc

                # Ensure the new cell is within bounds and has a height >= current cell
                if 0 <= new_r < rows and 0 <= new_c < cols and heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c, visited)

        # Perform DFS from all cells adjacent to the Pacific and Atlantic oceans
        for c in range(cols):
            dfs(0, c, pacific)         # From the top row (Pacific)
            dfs(rows - 1, c, atlantic) # From the bottom row (Atlantic)

        for r in range(rows):
            dfs(r, 0, pacific)         # From the left column (Pacific)
            dfs(r, cols - 1, atlantic) # From the right column (Atlantic)

        # Return the intersection of both reachable areas (Pacific & Atlantic)
        return list(pacific & atlantic)
