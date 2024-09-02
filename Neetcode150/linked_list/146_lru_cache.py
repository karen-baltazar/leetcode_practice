class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        """
        Hint: Use a combination of a doubly linked list and a hash map to maintain 
        the order of access and efficiently retrieve, insert, and remove elements.
        """
        self.cap = capacity
        self.cache = {}  # Maps key to the corresponding node in the linked list
        self.left, self.right = Node(0, 0), Node(0, 0)  # Dummy nodes to represent the bounds
        self.left.next, self.right.prev = self.right, self.left  # Initialize the list as empty

    def remove(self, node):
        prev, nxt = node.prev, node.next  # Get the previous and next nodes
        prev.next, nxt.prev = nxt, prev  # Bypass the node to remove it from the list

    def insert(self, node):
        prev, nxt = self.right.prev, self.right  # The node before right and right itself
        prev.next = nxt.prev = node  # Place the node between prev and nxt
        node.next, node.prev = nxt, prev  # Link the node back to prev and nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])  # If the key exists, remove the old node

        self.cache[key] = Node(key, value)  # Insert the new node with the updated value
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # If the cache exceeds its capacity, remove the least recently used item
            lru = self.left.next  # The first real node after left is the least recently used
            self.remove(lru)
            del self.cache[lru.key]  # Remove it from the hashmap as well
