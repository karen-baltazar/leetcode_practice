class Solution(object):
    def buildTree(self, inorder, postorder):
        # If either inorder or postorder is empty, return None
        if not inorder or not postorder:
            return None

        # The last element in postorder is the root of the tree
        root = TreeNode(postorder[-1])
        # Find the index of the root in inorder to split left and right subtrees
        mid = inorder.index(postorder[-1])

        # Recursively build the left and right subtrees
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid: -1])

        return root
