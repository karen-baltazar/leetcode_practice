class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()  # Sort coins to break early when a coin is too large
        dp = [0] * (amount + 1)  # Initialize DP array to store the minimum coins for each amount

        # Iterate over all amounts from 1 to the target amount
        for curr_amount in range(1, amount + 1):
            min_coins = float('inf')  # Initialize with infinity, to find the minimum later

            # Check each coin
            for coin in coins:
                remaining = curr_amount - coin  # Calculate the remaining amount if we use this coin
                if remaining < 0:
                    break  # Break early if the coin is larger than the current amount
                min_coins = min(min_coins, dp[remaining] + 1)  # Find the minimum coins required
            
            dp[curr_amount] = min_coins  # Store the minimum coins for the current amount

        # Return the result for the target amount, or -1 if it's not possible
        return dp[amount] if dp[amount] != float('inf') else -1
