import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []  # Min-heap to keep the k largest elements.

        for num in nums:
            # Add to heap if size < k, else replace the smallest.
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)  # Maintain k largest elements.

        return min_heap[0]  # The root is the k-th largest element.
