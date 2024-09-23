class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If the tree is empty, return an empty list
        if not root:
            return []
        
        queue = deque([root])  # Queue for level order traversal
        right_view = []  # List to store the right side view of the tree

        # Traverse each level of the tree
        while queue:
            rightmost_node = None  # To track the rightmost node at the current level

            for _ in range(len(queue)):
                node = queue.popleft()  # Remove node from the queue
                rightmost_node = node  # Update rightmost node to the current node

                # Add the left child if it exists
                if node.left:
                    queue.append(node.left)
                # Add the right child if it exists
                if node.right:
                    queue.append(node.right)

            # Add the rightmost node of the current level to the result
            right_view.append(rightmost_node.val)

        return right_view
