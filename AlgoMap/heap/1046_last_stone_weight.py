import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate weights to use a min-heap as a max-heap.
        stones = [-stone for stone in stones]
        heapq.heapify(stones)  # Create the heap.

        while len(stones) > 1:
            x = heapq.heappop(stones)  # Get the heaviest stone.
            y = heapq.heappop(stones)  # Get the second heaviest.

            # If they are not equal, push the difference back.
            if x != y:
                heapq.heappush(stones, x - y)

        return -stones[0] if stones else 0
