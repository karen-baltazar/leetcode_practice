class TimeMap:
    # Hint: Utilize binary search to efficiently find the closest timestamp less than or equal to the given one.

    def __init__(self):
        # Dictionary to store keys, each associated with a list of [value, timestamp] pairs
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        result = ""
        # Get the list of [value, timestamp] pairs for the key, or an empty list if the key does not exist
        values = self.store.get(key, [])

        # Binary search to find the closest timestamp <= given timestamp
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                # If the timestamp at mid is <= given timestamp, store the value and move right
                result = values[mid][0]
                left = mid + 1
            else:  
                # If the timestamp at mid is greater, move left
                right = mid - 1
        
        return result
