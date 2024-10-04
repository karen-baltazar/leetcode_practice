class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Hint: Use Union-Find (Disjoint Set Union) to detect cycles in the graph.
        # A cycle is detected when both nodes of an edge belong to the same component.

        n = len(edges)
        parent = [i for i in range(n)]  # Each node starts as its own parent
        rank = [1] * n  # Rank helps keep the tree balanced

        # Find function with path compression
        def find(node):
            root = node
            # Path compression: flatten the tree by linking nodes directly to their grandparent
            while root != parent[root]:
                parent[root] = parent[parent[root]]
                root = parent[root]
            return root

        # Union function to join two components
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)

            # If both nodes share the same root, a cycle is found
            if root1 == root2:
                return False

            # Union by rank: attach the smaller tree to the larger one
            if rank[root2] > rank[root1]:
                parent[root1] = root2
                rank[root2] += rank[root1]
            else:
                parent[root2] = root1
                rank[root1] += rank[root2]

            return True

        # Process each edge in the graph
        for node1, node2 in edges:
            # If union fails, this is the redundant edge that forms a cycle
            if not union(node1 - 1, node2 - 1):
                return [node1, node2]
