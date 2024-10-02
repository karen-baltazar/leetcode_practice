class Solution:
    def validPath(self, n: int, edges: List[List[int]], src: int, dst: int) -> bool:
        # Create an adjacency list representation of the graph
        graph = defaultdict(list)

        # Build the graph from the edges
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Set to track visited nodes
        visited = set()
        visited.add(src)

        # Stack for DFS traversal, starting from the source node
        stack = [src]

        # Perform DFS
        while stack:
            node = stack.pop()  # Current node to explore
            # Explore neighbors of the current node
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        # Check if the destination node was reached
        return dst in visited
