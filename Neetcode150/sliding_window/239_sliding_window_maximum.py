import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_values = []
        deque = collections.deque()  # Deque to store indices
        left = right = 0

        while right < len(nums):
            # Remove elements from deque that are smaller than the current element nums[right]
            while deque and nums[deque[-1]] < nums[right]:
                deque.pop()
            deque.append(right)

            # Remove the leftmost element from deque if it is out of the current window
            if left > deque[0]:
                deque.popleft()

            # Once we've filled the first window, start adding max values to the output
            if (right + 1) >= k:
                max_values.append(nums[deque[0]])
                left += 1

            right += 1

        return max_values
