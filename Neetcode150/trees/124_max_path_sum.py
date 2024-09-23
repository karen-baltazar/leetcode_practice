class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # List to keep track of the maximum path sum found so far
        max_path_sum = [root.val]
        
        # Helper function to perform DFS and calculate the max path sum
        def calculateMaxPath(node):
            if not node:
                return 0

            # Calculate max path sum for the left and right subtrees, ignoring negative sums
            max_left = max(0, calculateMaxPath(node.left))
            max_right = max(0, calculateMaxPath(node.right))
            
            # Update the global max path sum with the current node as the highest root
            max_path_sum[0] = max(max_path_sum[0], max_left + max_right + node.val)
            
            # Return the max sum path including the current node
            return node.val + max(max_left, max_right)

        # Start the DFS traversal from the root
        calculateMaxPath(root)
        
        return max_path_sum[0]
