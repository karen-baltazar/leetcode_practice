class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty set to keep track of the unique numbers encountered.
        hashset = set()

        # Iterate through each number in the input list.
        for n in nums:
            # If the current number is already in the set, it means we have found a duplicate.
            if n in hashset:
                return True
            # Otherwise, add the current number to the set.
            hashset.add(n)
        
        # If no duplicates are found during the loop, return False.
        return False
