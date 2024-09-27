from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curr = [], []  # res stores the combinations, curr stores the current path
        nums = sorted(candidates)  # Sort to handle duplicates and manage combinations
        n = len(nums)

        def backtrack(i, total):
            # If the total matches the target, add the current combination
            if total == target:
                res.append(curr[:])  # Append a copy of curr
                return

            if i == n:
                return

            # If adding the current number keeps the total within target, proceed
            if total + nums[i] <= target:
                curr.append(nums[i])
                backtrack(i + 1, total + nums[i])  # Explore with the current number included
                curr.pop()  # Backtrack to explore other options

            # Skip duplicates by moving index past duplicates
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, total)  # Explore without the current number

        backtrack(0, 0)
        return res
