class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, trees are identical up to this point
        if not p and not q:
            return True
        
        # If one node is None or values do not match, trees are not identical
        if not p or not q or p.val != q.val:
            return False

        # Recursively check if the left and right subtrees are the same
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        # Trees are the same if both left and right subtrees match
        return left_same and right_same
