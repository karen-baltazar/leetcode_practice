class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of the numbers we've seen
        prevMap = {}

        # Iterate through the list with both index and value
        for i, n in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - n
            
            # Check if the difference is already in the dictionary
            if diff in prevMap:
                # If it is, we found the two numbers that sum up to the target
                return [prevMap[diff], i]

            # Store the index of the current number
            prevMap[n] = i
