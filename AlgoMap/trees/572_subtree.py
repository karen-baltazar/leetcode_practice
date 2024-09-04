class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_identical(tree1, tree2):
            # If both nodes are None, trees are identical
            if not tree1 and not tree2:
                return True
            # If one node is None or values don't match, trees are not identical
            if not tree1 or not tree2 or tree1.val != tree2.val:
                return False
            # Recursively check left and right subtrees
            return (is_identical(tree1.left, tree2.left) and
                    is_identical(tree1.right, tree2.right))

        if not root:
            return False

        # Check if the current node is the root of an identical subtree
        if is_identical(root, subRoot):
            return True
        
        # Recursively check left and right subtrees
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
