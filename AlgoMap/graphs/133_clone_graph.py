class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}  # Dictionary to map original nodes to their clones

        # Depth-First Search (DFS) to clone the graph
        def dfs(node):
            # If the node has already been cloned, return the clone
            if node in old_to_new:
                return old_to_new[node]

            # Create a new node (clone) with the same value as the original node
            clone = Node(node.val)
            old_to_new[node] = clone

            # Recursively clone all the neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone

        # Return the cloned graph starting from the given node, or None if node is None
        return dfs(node) if node else None
