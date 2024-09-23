class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: if either traversal is empty, return None
        if not preorder or not inorder:
            return None

        # The first element in preorder is the root of the current subtree
        root = TreeNode(preorder[0])
        
        # Find the index of the root in inorder to split left and right subtrees
        root_index_in_inorder = inorder.index(preorder[0])

        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder[1: root_index_in_inorder + 1], inorder[:root_index_in_inorder])
        root.right = self.buildTree(preorder[root_index_in_inorder + 1:], inorder[root_index_in_inorder + 1:])

        return root
