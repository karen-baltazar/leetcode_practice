class Solution(object):
    def removeElement(self, nums, val):
        j = len(nums) - 1
        i = 0
        
        while j >= 0 and j >= i:
            if nums[j] == val:
                j = j - 1
            elif nums[i] == val:
                nums[i] = nums[j]
                i = i + 1
                j = j - 1 
            else:
                i = i + 1

        return i