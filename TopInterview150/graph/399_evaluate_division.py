from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Hint: Use an adjacency list to represent the graph. Each node points to its neighbors with the corresponding division value.

        # Create an adjacency list to represent the graph
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1 / values[i]])

        # Breadth-First Search (BFS) to find the path and calculate the division
        def bfs(src, target):
            # If either source or target node doesn't exist in the graph, return -1
            if src not in adj or target not in adj:
                return -1

            # Queue for BFS and set for visited nodes
            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)

            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)
            return -1

        # Evaluate each query using BFS
        return [bfs(q[0], q[1]) for q in queries]

# Note: BFS is used here instead of DFS because BFS can find the shortest path in an unweighted graph. 
# This is particularly useful when we want to ensure the fewest multiplications or divisions to get from the source to the target.
