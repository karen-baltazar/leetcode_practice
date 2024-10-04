from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Hint: Use DFS to detect cycles and ensure all nodes are connected.
        # prev_node helps avoid counting the edge from the current node back to its parent.

        # Build the adjacency list representation of the graph
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # A valid tree must be acyclic and connected
        visited = set()
        stack = [(0, -1)]  # (current node, previous node)

        while stack:
            node, prev_node = stack.pop()

            if node in visited:
                # Cycle detected if a node is visited again
                return False

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor != prev_node:
                    # Explore the next node, ignoring the edge that leads back to the parent
                    stack.append((neighbor, node))

        # Check if the graph is connected (all nodes must be visited)
        return len(visited) == n
