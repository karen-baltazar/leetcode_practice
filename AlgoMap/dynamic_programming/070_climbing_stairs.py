class Solution:
    def climbStairs(self, n: int) -> int:        
        if n == 1:
            return 1  # If there's only one step, only one way to climb.

        if n == 2:
            return 2  # If there are two steps, two ways (1+1 or 2).

        # Initialize variables for the previous two steps
        prev, cur = 1, 2

        # For each step from 3 to n, the number of ways to reach that step
        # is the sum of the ways to reach the two previous steps.
        for i in range(2, n):
            prev, cur = cur, prev + cur  # Move the window to calculate the next step.

        return cur  # Return the number of ways to climb n steps.
