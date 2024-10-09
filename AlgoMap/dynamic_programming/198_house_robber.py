class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # If there's only one house, the maximum money robbed is from that house.
        if n == 1:
            return nums[0]

        # If there are two houses, rob the house with the maximum money.
        if n == 2:
            return max(nums[0], nums[1])

        # Initialize prev to track the money robbed up to two houses before,
        # and cur for the previous house's max money robbed.
        prev, cur = nums[0], max(nums[0], nums[1])

        # Iterate through the rest of the houses starting from the third house.
        for i in range(2, n):
            # Update prev and cur to store the max money if robbing this house or skipping it.
            prev, cur = cur, max(nums[i] + prev, cur)

        # The final value in cur will hold the maximum money that can be robbed.
        return cur
