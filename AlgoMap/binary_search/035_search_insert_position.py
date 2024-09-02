class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Hint: This problem is an extension of binary search, 
        # where you return the index where the target would be inserted if not found.
        low, high = 0, len(nums) - 1
        
        while low <= high:        
            mid = (low + high) // 2  
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        # If target is not found, determine its insert position
        if target > nums[mid]:
            return mid + 1
        else:
            return mid