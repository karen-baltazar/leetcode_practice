class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Hint: Use a set to store elements and check for consecutive sequences.
        
        # Convert the list into a set for O(1) access
        numSet = set(nums)
        longest = 0  # Variable to store the length of the longest sequence

        for n in nums:
            # Check if it is the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:  # Count the length of the sequence
                    length += 1

                longest = max(length, longest)  # Update the longest sequence length

        return longest
