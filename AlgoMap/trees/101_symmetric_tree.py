class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def same(l_node, r_node):
            # If both nodes are None, they are symmetric
            if not l_node and not r_node:
                return True

            # If one node is None or their values don't match, they are not symmetric
            if not l_node or not r_node or l_node.val != r_node.val:
                return False

            # Recursively compare opposite subtrees
            out_side = compare(l_node.left, r_node.right)
            in_side = compare(l_node.right, r_node.left)

            # Both outside and inside comparisons must be true for the tree to be symmetric
            return out_side and in_side

        # Start the comparison from the left and right children of the root
        return same(root.left, root.right)
