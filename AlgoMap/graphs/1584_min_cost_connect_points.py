class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Hint: We are using Prim's Algorithm to find the Minimum Spanning Tree (MST)
        n = len(points)
        total_cost = 0
        visited = set()
        
        # Min-heap to keep track of the minimum cost edge to add to the MST
        # Starting with point 0 at distance 0
        min_heap = [(0, 0)]  # (cost, point_index)

        # While there are unvisited points
        while len(visited) < n:
            # Get the smallest distance edge from the heap
            dist, i = heapq.heappop(min_heap)

            # If the point has already been visited, skip
            if i in visited:
                continue

            visited.add(i)
            total_cost += dist
            xi, yi = points[i]

            # Check all other points and calculate the Manhattan distance
            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    nei_dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(min_heap, (nei_dist, j))

        return total_cost
