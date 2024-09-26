class MedianFinder:

    def __init__(self):
        self.max_heap, self.min_heap = [], []  # max_heap for the lower half, min_heap for the upper half

    def addNum(self, num: int) -> None:
        # Add the number to max_heap (inverted to act as max heap)
        heapq.heappush(self.max_heap, -num)

        # Ensure all elements in max_heap are less than elements in min_heap
        if self.max_heap and self.min_heap and (-self.max_heap[0]) > self.min_heap[0]:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # Balance the heaps if max_heap has more than one extra element
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        # Balance the heaps if min_heap has more than one extra element
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)    

    def findMedian(self) -> float:
        # If max_heap has more elements, the median is its root
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        # If min_heap has more elements, the median is its root
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        # If heaps are balanced, the median is the average of both roots
        return (-self.max_heap[0] + self.min_heap[0]) / 2
