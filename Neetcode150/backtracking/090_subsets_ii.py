class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []  # Initialize the result list and the current subset
        n = len(nums)
        nums.sort()  # Sort the input to handle duplicates

        def backtrack(index):
            # If we've considered all numbers, add the current subset to results
            if index == n:
                res.append(subset[:])  # Append a copy of the current subset
                return

            # Include the current number in the subset
            subset.append(nums[index])
            backtrack(index + 1)  # Move to the next index
            subset.pop()  # Backtrack: remove the last added number

            # Skip duplicates
            while index + 1 < n and nums[index] == nums[index + 1]:
                index += 1  # Increment index to skip duplicates

            backtrack(index + 1)  # Explore without the current number

        backtrack(0)  # Start backtracking from the first index
        return res  # Return the complete list of subsets
