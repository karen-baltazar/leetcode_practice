class Solution(object):
    def invertTree(self, root):
        # Recursive approach to invert a binary tree
        if root:
            # Swap the left and right children
            temp = root.left
            root.left = root.right
            root.right = temp

            # Recursively invert the left and right subtrees
            self.invertTree(root.right)
            self.invertTree(root.left)

        return root

    def invertTreeIterative(self, root):
        # Iterative approach to invert a binary tree using a stack
        if not root:
            return root
        
        stack = [root]
        
        while stack:
            curr = stack.pop()
            # Swap the left and right children
            curr.left, curr.right = curr.right, curr.left
            
            # Add the left child to the stack if it exists
            if curr.left:
                stack.append(curr.left)
            
            # Add the right child to the stack if it exists
            if curr.right:                
                stack.append(curr.right)
        
        return root
