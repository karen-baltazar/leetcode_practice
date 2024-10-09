class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1  # Set the initial target as the last index

        # Iterate backwards through the list, checking if we can reach the target
        for i in range(target - 1, -1, -1):
            # If the current number is sufficient to reach or pass the target
            if nums[i] >= (target - i):
                target = i  # Update the target to the current index
        
        # If the target reaches the start, return True
        return target == 0
