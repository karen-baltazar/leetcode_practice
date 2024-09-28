class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, perm = [], []

        def backtrack():
            if len(perm) == n:
                res.append(perm[:])  # Store a copy of the current permutation
                return

            used = set(perm)  # Track used numbers

            for num in nums:
                if num not in used:  # Only consider unused numbers
                    perm.append(num)
                    backtrack()  # Recursively build the permutation
                    perm.pop()

        backtrack()
        return res
