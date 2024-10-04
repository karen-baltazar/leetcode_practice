class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Hint: Use the Union-Find (Disjoint Set Union) algorithm. This approach helps to track connected components efficiently.
        
        # Parent array initialized with each node as its own parent
        parent = [i for i in range(n)]
        # Rank array initialized with 1 for each node, used to keep the tree balanced
        rank = [1] * n

        def find(node):
            # Find the root of the set, applying path compression
            root = node
            while root != parent[root]:
                # Path compression: point the node directly to its grandparent
                parent[root] = parent[parent[root]]
                root = parent[root]
            return root

        def union(node1, node2):
            # Find the root of both nodes
            root1, root2 = find(node1), find(node2)

            # If they have the same root, they're already connected
            if root1 == root2:
                return 0

            # Union by rank: attach the smaller tree under the larger tree
            if rank[root2] > rank[root1]:
                parent[root1] = root2
                rank[root2] += rank[root1]
            else:
                parent[root2] = root1
                rank[root1] += rank[root2]
            
            return 1

        # Initially, we have 'n' components, so we subtract each time we merge two components
        components = n
        for node1, node2 in edges:
            components -= union(node1, node2)

        return components
