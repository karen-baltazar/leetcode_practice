class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time, fresh_count = 0, 0
        queue = deque()

        # Count fresh oranges and add rotten ones to the queue
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_count += 1  # Counting fresh oranges
                if grid[row][col] == 2:
                    queue.append((row, col))  # Add rotten oranges to the queue

        # Process the rotten oranges in BFS manner
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # Check all four neighbors (right, left, down, up)
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    # If the neighbor is a fresh orange, rot it
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2  # Mark orange as rotten
                        fresh_count -= 1  # Decrease the count of fresh oranges

            time += 1  # Increment time after processing all rotten oranges

        # Return time if all fresh oranges are rotten, otherwise return -1
        return time if fresh_count == 0 else -1
