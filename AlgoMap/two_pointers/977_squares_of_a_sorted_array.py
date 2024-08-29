class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Hint: Use two pointers, one at the start and one at the end of the array.

        res = [] 
        left, right = 0, len(nums) - 1 

        # While the pointers have not crossed
        while left <= right:
            # Add the square of the larger number to the result list
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] ** 2) 
                left += 1 
            else:
                res.append(nums[right] ** 2) 
                right -= 1 

        return res[::-1]  # Reverse the list to get it in ascending order
