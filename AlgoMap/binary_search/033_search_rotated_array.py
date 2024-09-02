class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # Step 1: Find the index of the smallest element (pivot)
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        min_i = left

        # Step 2: Determine the search bounds based on the target
        if min_i == 0:
            # If the array is not rotated, search the entire array
            left, right = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[min_i - 1]:
            left, right = 0, min_i - 1
        else:
            left, right = min_i, len(nums) - 1

        # Step 3: Perform binary search within the identified bounds
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid  
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1 

        return -1
