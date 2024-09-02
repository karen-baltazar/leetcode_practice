class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Hint: Treat the array as a linked list where each index points to the next node. 
        # Use Floyd's Tortoise and Hare algorithm to find the duplicate.

        # Initialize two pointers
        tortoise, hare = 0, 0

        # First phase: Find the intersection point in the cycle
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Second phase: Find the entrance to the cycle (duplicate number)
        pointer1 = 0
        while True:
            tortoise = nums[tortoise]
            pointer1 = nums[pointer1]
            if tortoise == pointer1:
                return tortoise
