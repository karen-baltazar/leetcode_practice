class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the tree is empty, return depth 0
        if not root:
            return 0

        # Recursively find the depth of the left and right subtrees
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # The depth of the current node is 1 plus the maximum depth of its subtrees
        return 1 + max(left, right)
