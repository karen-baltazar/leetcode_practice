class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Hint: Use an inorder traversal to process the nodes in sorted order
        min_distance = [float('inf')]
        prev = [None]

        def dfs(node):
            if not node:
                return  
            # Traverse the left subtree first
            dfs(node.left)

            # If the previous node exists, calculate the difference and update the minimum distance
            if prev[0] is not None:
                min_distance[0] = min(min_distance[0], node.val - prev[0])

            # Update the previous node to the current node's value
            prev[0] = node.val

            # Traverse the right subtree
            dfs(node.right)

        dfs(root)
        return min_distance[0]
