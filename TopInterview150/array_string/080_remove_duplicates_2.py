class Solution(object):
    def removeDuplicates(self, nums):
        """
        Hint: Utilize two pointers to track unique elements and the number of consecutive duplicates. 
        Then, copy at most 2 duplicates to the result while iterating over the array.
        """

        # Initialize left and right pointers
        l = 0
        r = 0

        # Iterate over the array
        while r < len(nums):
            # Initialize count to track number of consecutive duplicates
            count = 1

            # Count consecutive duplicates
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                count += 1

            # Copy at most 2 duplicates to the result
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1

            # Move to the next element
            r += 1

        # Return the length of the resulting array
        return l
