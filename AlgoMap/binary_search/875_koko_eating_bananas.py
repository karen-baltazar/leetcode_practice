from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Hint: Consider using binary search to minimize the range of possible eating speeds.

        def canFinish(speed):
            total_hours = 0
            for pile in piles:
                total_hours += ceil(pile / speed)
            return total_hours <= h

        low, high = 1, max(piles)

        while low < high:
            mid_speed = (low + high) // 2

            if canFinish(mid_speed):
                high = mid_speed  # Try a slower speed
            else:
                low = mid_speed + 1  # Increase speed

        return low