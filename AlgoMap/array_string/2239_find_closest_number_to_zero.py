class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Hint: Track the number with the smallest absolute value while iterating through the list.
        
        # Initialize with the first element of the list
        closest = nums[0]

        for n in nums:
            # Update closest if a smaller absolute value is found
            if abs(n) < abs(closest):
                closest = n
            # If there is a tie, prefer the positive number
            elif abs(n) == abs(closest) and n > closest:
                closest = n

        return closest
