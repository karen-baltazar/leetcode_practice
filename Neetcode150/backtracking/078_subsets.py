class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, subset = [], []

        def backtrack(index):
            if index == n:
                res.append(subset[:])
                return

            backtrack(index + 1)  # Exclude current number

            subset.append(nums[index])  # Include current number
            backtrack(index + 1)  # Move to the next
            subset.pop()  # Backtrack

        backtrack(0)
        return res
