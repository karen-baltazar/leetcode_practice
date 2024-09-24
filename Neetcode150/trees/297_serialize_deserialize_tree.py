class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serialized_tree = []

        # Helper function for DFS traversal to serialize the tree
        def traverse(node):
            if not node:
                serialized_tree.append("N")  # N represents a null node
                return

            # Append the current node's value
            serialized_tree.append(str(node.val))

            # Recursively serialize the left and right subtrees
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        
        # Join the values with commas for compact representation
        return ",".join(serialized_tree)      

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",")
        self.index = 0

        # Helper function to build the tree using DFS
        def buildTree():
            if values[self.index] == "N":
                self.index += 1
                return None

            # Create a new node with the current value
            current_node = TreeNode(int(values[self.index]))
            self.index += 1

            # Recursively build the left and right subtrees
            current_node.left = buildTree()
            current_node.right = buildTree()

            return current_node

        return buildTree()
