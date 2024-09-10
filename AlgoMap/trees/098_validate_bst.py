class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to validate the BST
        def validate(node, lower_bound, upper_bound):
            # If node is None, it's a valid BST by default
            if not node:
                return True

            # The current node's value must be within the bounds
            if node.val <= lower_bound or node.val >= upper_bound:
                return False

            # Recursively validate left and right subtrees
            return validate(node.left, lower_bound, node.val) and validate(node.right, node.val, upper_bound)

        # Start the validation with initial bounds (-infinity, infinity)
        return validate(root, float('-inf'), float('inf'))
