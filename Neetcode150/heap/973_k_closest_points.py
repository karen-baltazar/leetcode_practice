from typing import List
import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []  # Min-heap to store the k closest points

        for x, y in points:
            dist = -sqrt(x ** 2 + y ** 2)  # Use negative distance for max-heap behavior
            
            if len(heap) < k:
                heapq.heappush(heap, (dist, (x, y)))  # Push the point with its distance
            else:
                heapq.heappushpop(heap, (dist, (x, y)))  # Replace if current point is closer

        return [h[1] for h in heap]  # Return the points only
