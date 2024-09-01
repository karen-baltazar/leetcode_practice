"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a map to store the mapping from original nodes to their copies
        node_map = {}
        
        # First pass: create a copy of each node and store it in the map
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next
        
        # Second pass: set the next and random pointers for each copied node
        current = head
        while current:
            copy = node_map[current]
            copy.next = node_map.get(current.next)  # Use get() to handle None
            copy.random = node_map.get(current.random)  # Use get() to handle None
            current = current.next
        
        return node_map.get(head)  # Return the head of the copied list