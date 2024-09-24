class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k] # Track the number of nodes we've processed
        result = [0] # Store kth smallest element once found

        def dfs(node):
            # Base case: if the node is None, return
            if not node:
                return
            
            # Recursively traverse the left subtree
            dfs(node.left)
            
            # After visiting the left subtree, decrease count by 1
            count[0] -= 1
            
            # If count reaches 0, we've found the kth smallest element
            if count[0] == 0:
                result[0] = node.val
                return
            
            # Recursively traverse the right subtree if needed
            dfs(node.right)

        dfs(root)
        return result[0]
