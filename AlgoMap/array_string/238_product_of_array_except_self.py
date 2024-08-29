class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Hint: Use prefix and postfix products to avoid division.

        # Initialize the result array with 1s
        res = [1] * len(nums)

        # Calculate prefix products
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Calculate postfix products and update the result array
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
