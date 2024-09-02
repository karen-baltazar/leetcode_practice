class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum value must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum value is in the left half
            else:
                right = mid

        # At the end of the loop, left and right converge to the minimum element
        return nums[left]
