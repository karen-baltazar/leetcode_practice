class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        l = len(nums)
        
        for j in range(1, l):       
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]

        return i + 1
