from typing import List
import heapq

class KthLargest: 
    def __init__(self, k: int, nums: List[int]):
        self.heap = []  # Min-heap to store the k largest elements
        self.k = k  # The k value

        # Initialize the heap with the first k elements
        for num in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)  # Add element to heap
            elif num > self.heap[0]:  # If current number is larger than the smallest in heap
                heapq.heappushpop(self.heap, num)  # Replace the smallest

    def add(self, val: int) -> int:
        # Add new value and maintain the heap size
        if len(self.heap) < self.k:  # If the heap has fewer than k elements
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:  # If new value is larger than the smallest
            heapq.heappushpop(self.heap, val)  # Replace the smallest
        
        return self.heap[0]  # The kth largest element
