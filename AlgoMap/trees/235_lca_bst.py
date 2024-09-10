class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Hint: In a BST, the LCA is the node where the paths to p and q diverge
        lca = [root]

        def search(node):
            if not node:
                return

            # Update the current lowest common ancestor
            lca[0] = node

            # If we find either p or q, we stop further searching
            if node is p or node is q:
                return
            
            # If both p and q are larger, move to the right subtree
            if node.val < p.val and node.val < q.val:
                search(node.right)
            # If both p and q are smaller, move to the left subtree
            elif node.val > p.val and node.val > q.val:
                search(node.left)
            # If the current node is between p and q, it is the LCA
            else:
                return
        
        search(root)
        return lca[0]
