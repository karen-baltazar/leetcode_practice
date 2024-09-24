class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # List to store the largest diameter found
        max_diameter = [0]

        def height(node):
            if not node:
                return 0

            # Recursively find the height of the left and right subtrees
            left_h = height(node.left)
            right_h = height(node.right)

            # Calculate the diameter passing through the current node
            diameter = left_h + right_h

            # Update the maximum diameter found
            max_diameter[0] = max(max_diameter[0], diameter)

            # Return the height of the current node
            return 1 + max(left_h, right_h)

        # Calculate height starting from the root
        height(root)
        return max_diameter[0]
