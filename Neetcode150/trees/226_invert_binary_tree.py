class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the root of the inverted tree
        return root
