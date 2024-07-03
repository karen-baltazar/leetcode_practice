class Solution(object):
    def isSameTree(self, p, q):
        # If both nodes are None, they are the same
        if not p and not q:
            return True
        
        # If one node is None and the other is not, or the values are different, they are not the same
        if not p or not q or p.val != q.val:
            return False

        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
