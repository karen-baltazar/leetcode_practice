class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        # Hint: Use a DFS approach to traverse the tree and track the maximum value seen so far.
        good_node_count = [0]

        # Helper function for DFS traversal
        def dfs(node, max_val):
            # Base case: if the node is None, return
            if not node:
                return

            # If the current node's value is greater than or equal to max_val, it's a good node
            if node.val >= max_val:
                good_node_count[0] += 1

            # Traverse left and right subtrees, updating the max value seen so far
            dfs(node.left, max(max_val, node.val))
            dfs(node.right, max(max_val, node.val))

        dfs(root, root.val)
        return good_node_count[0]
