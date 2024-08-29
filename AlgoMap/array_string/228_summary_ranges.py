class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Hint: Use a while loop to find continuous ranges and store them.
        
        res = []  # List to store the resulting ranges
        i = 0 

        while i < len(nums): 
            start = nums[i]  # Start of the current range

            # Find the end of the current range
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1

            # If start is different from end, it's a range
            if start != nums[i]:
                res.append(str(start) + "->" + str(nums[i]))
            else:  # If start is equal to end, it's a single number
                res.append(str(nums[i]))

            i += 1  # Move to the next element

        return res