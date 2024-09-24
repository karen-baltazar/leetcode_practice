class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Use a list to track if the tree is balanced
        balanced = [True]

        def height(node):
            if not node:
                return 0

            # Recursively find the height of the left subtree
            left_h = height(node.left)
            
            if not balanced[0]:
                return 0

            # Recursively find the height of the right subtree
            right_h = height(node.right)

            # If the difference in heights is greater than 1, mark the tree as unbalanced
            if abs(left_h - right_h) > 1:
                balanced[0] = False
                return 0

            # Return the height of the current node
            return 1 + max(left_h, right_h)

        # Start the height calculation from the root
        height(root)
        return balanced[0]
