class Solution(object):
    def isSymmetric(self, root):
        def isMirror(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2 or tree1.val != tree2.val:
                return False
            
            # Check if the left subtree of tree1 is a mirror of the right subtree of tree2, and vice versa
            return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)
        
        # Start the recursion with the left and right children of the root
        return isMirror(root.left, root.right)
