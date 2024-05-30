"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Hint: Use DFS to traverse and clone the graph. Also use a dictionary to map original nodes to their copies.

        # Dictionary to map original nodes to their copies
        oldToNew = {}

        def dfs(node):
            # If the node is already copied, return the copy
            if node in oldToNew:
                return oldToNew[node]

            # Create a copy of the node
            copy = Node(node.val)
            # Store the copy in the dictionary
            oldToNew[node] = copy

            # Recursively copy all the neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        # Return the result of dfs if the input node is not None
        return dfs(node) if node else None
