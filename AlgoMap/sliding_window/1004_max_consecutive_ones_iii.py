class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0  # Start of the sliding window
        zero_count = 0  # Number of zeros in the current window
        max_len = 0  # Maximum length of subarray with at most k zeros

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # If there are more than 'k' zeros, shrink the window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update the maximum length of the window
            max_len = max(max_len, right - left + 1)

        return max_len
