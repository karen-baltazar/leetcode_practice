class Solution(object):
    def minSubArrayLen(self, target, nums):
        min_length = float('inf')
        left = 0 # Left pointer of the window
        nsum = 0 # Current sum of the window

        # Iterate over nums with the index and value
        for i, n in enumerate(nums):
            nsum += n

            # While the current sum is greater than or equal to target
            while nsum >= target:
                # Update the minimum length of the subarray
                min_length = min(min_length, i - left + 1)
                # Subtract the number at the left pointer from the current sum
                nsum -= nums[left]
                # Move the left pointer to the right
                left += 1

        # Return the minimum length if found, otherwise return 0
        return min_length if min_length != float('inf') else 0
