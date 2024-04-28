class Solution(object):
    def removeElement(self, nums, val):
        j = len(nums) - 1
        i = 0
        k = 0

        while j >= 0 and j >= i:
            if nums[j] == val:
                j = j - 1
            elif nums[i] == val:
                nums[i] = nums[j]
                nums[j] = val
                i = i + 1
                k = k + 1
                j = j - 1 
            else:
                i = i + 1
                k = k + 1 

        diff = len(nums) - k
        nums = nums[:diff]
        return k