class Solution:
    def fib(self, n: int) -> int:
        # Hint: This problem can be solved efficiently using dynamic programming (DP).
        # DP is used to store the results of subproblems, allowing us to avoid recalculating the same Fibonacci numbers.

        if n == 0:
            return 0  # Base case: F(0) = 0
        
        if n == 1:
            return 1  # Base case: F(1) = 1

        # Initialize a DP array to store Fibonacci numbers
        dp = [0] * (n + 1)
        dp[1] = 1  # F(1) = 1

        # Fill the DP array by adding previous two Fibonacci numbers
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]  # Return the nth Fibonacci number
