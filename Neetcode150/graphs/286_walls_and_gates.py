class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        # Constants to represent different entities on the grid
        EMPTY, GATE, WALL = 2147483647, 0, -1
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        dist = 1  # Initialize distance as 1

        # Add all gates to the queue to start BFS from them
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == GATE:
                    q.append((r, c))

        # BFS traversal to fill distances
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Continue if out of bounds or visiting non-empty cells
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != EMPTY:
                        continue

                    # Update the distance for empty rooms and add them to the queue
                    grid[nr][nc] = dist
                    q.append((nr, nc))

            dist += 1  # Increment distance for the next layer of BFS
