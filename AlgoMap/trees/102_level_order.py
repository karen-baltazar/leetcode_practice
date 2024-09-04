from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the root is None, return an empty list
        if not root:
            return []
        
        # Initialize a queue to perform BFS, starting with the root node
        queue = deque([root])
        result = []
        
        # Continue the BFS until the queue is empty
        while queue:
            level = []
            # Process all nodes at the current level
            for _ in range(len(queue)):
                node = queue.popleft()  # Dequeue a node
                level.append(node.val)  # Add its value to the current level list
                # Enqueue the left child if it exists
                if node.left:
                    queue.append(node.left)
                # Enqueue the right child if it exists
                if node.right:
                    queue.append(node.right)
            # Add the current level's values to the result list
            result.append(level)
        
        # Return the level order traversal result
        return result
