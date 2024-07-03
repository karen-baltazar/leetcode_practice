class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # If the node is None, the depth is 0
        if not root:
            return 0
        
        # Recursively find the depth of each subtree
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The depth of the tree rooted at the current node is the maximum of the depths
        # of the left and right subtrees, plus one for the current node
        return max(left_depth, right_depth) + 1
