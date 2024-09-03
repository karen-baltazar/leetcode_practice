class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize the sum of the first 'k' elements.
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Iterate over the array starting from the k-th element.
        for i in range(k, len(nums)):
            # Slide the window by subtracting the element going out and adding the element coming in.
            current_sum += nums[i] - nums[i - k]
            # Update the maximum sum found so far.
            max_sum = max(max_sum, current_sum)
        
        return max_sum / k
