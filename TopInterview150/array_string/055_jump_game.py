class Solution(object):
    def canJump(self, nums):
        # Hint: Start from the end and try to reach the start. At each step, check if the current position can reach the previous position.
        
        # Initialize pointers
        j = len(nums) - 1  # Pointer for the target position
        i = j - 1  # Pointer for the position to be checked
        
        # Iterate through the array from right to left
        while i >= 0:
            # If the current position can reach the target position, update the target position
            if nums[i] >= (j - i):
                j = i
            
            # Move to the previous position
            i -= 1
        
        # If the target position is 0, return True (able to reach the start), otherwise return False
        return True if j == 0 else False
