class Solution(object):
    def rotate(self, nums, k):
        # Hint: How can we adjust the value of k to ensure it's within the range of the list length?

        # Adjust k in case it's larger than the length of nums
        n = len(nums)
        k %= n

        # Rotate the list in-place
        nums[:] = nums[-k:] + nums[:-k]
        