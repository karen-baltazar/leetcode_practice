class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0  # Left pointer of the sliding window
        current_sum = 0  # Sum of the current window
        min_length = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]  # Expand the window by adding the current element

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)  # Update minimum length if current window is smaller
                current_sum -= nums[left]  # Shrink the window from the left
                left += 1  # Move the left pointer to the right

        return min_length if min_length != float('inf') else 0
