class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 1D array to track the number of ways to reach each cell in the first row
        dp = [1] * n

        # Loop over each row starting from the second one
        for i in range(1, m):
            # Loop over each column starting from the second one
            for j in range(1, n):
                # Update dp[j] by adding the value from the left (dp[j-1]) to it (previous row)
                dp[j] = dp[j - 1] + dp[j]

        # Return the value at the last cell which contains the total unique paths
        return dp[n - 1]
