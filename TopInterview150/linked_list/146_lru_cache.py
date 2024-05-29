from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # Hint: Use an OrderedDict to maintain the order of elements based on their usage.
        self.cache = OrderedDict()  # OrderedDict to store the cache
        self.capacity = capacity    # Maximum capacity of the cache
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # Key not found, return -1
        else:
            # Move the accessed key to the end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]  # Return the value associated with the key
        

    def put(self, key: int, value: int) -> None:
        # Insert or update the key with the given value
        self.cache[key] = value
        # Move the key to the end (most recently used)
        self.cache.move_to_end(key)

        # If the cache exceeds the capacity, remove the least recently used item
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove the first item (least recently used)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
