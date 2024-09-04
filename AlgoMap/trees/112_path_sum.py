class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def check_path(node, current_sum):
            # Base case: if node is None, return False
            if not node:
                return False

            # Update current sum with the node's value
            current_sum += node.val

            # If leaf node is reached, check if current sum equals targetSum
            if not node.left and not node.right:
                return current_sum == targetSum

            # Recursively check left and right subtrees
            return (check_path(node.left, current_sum) or
                    check_path(node.right, current_sum))

        # Start checking from the root with initial sum 0
        return check_path(root, 0)
