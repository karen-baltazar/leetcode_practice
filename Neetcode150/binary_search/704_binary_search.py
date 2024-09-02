class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Hint: This algorithm divides the search space by half each time, 
        # making it efficient for sorted arrays.
        low, high = 0, len(nums) - 1
        
        while low <= high:        
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1