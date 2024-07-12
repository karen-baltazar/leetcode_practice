class Solution(object):
    def buildTree(self, preorder, inorder):
        # If either preorder or inorder is empty, return None
        if not preorder or not inorder:
            return None

        # The first element of preorder is the root of the tree
        root = TreeNode(preorder[0])

        # Find the index of the root in inorder to split the tree into left and right subtrees
        mid = inorder.index(preorder[0])

        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
