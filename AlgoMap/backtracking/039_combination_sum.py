from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path = [], []  # `res` stores valid combinations; `path` tracks current combination
        n = len(nums)  # Total number of candidates

        def backtrack(i, total):
            if total == target:  # Found a valid combination
                res.append(path[:])
                return
            if total > target or i == n:  # Exceeded target or end of list
                return

            # Skip the current number
            backtrack(i + 1, total)

            # Include the current number and backtrack
            path.append(nums[i])
            backtrack(i, total + nums[i])
            path.pop()  # Backtrack

        backtrack(0, 0)
        return res
