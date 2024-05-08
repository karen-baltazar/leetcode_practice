class Solution(object):
    def maxProfit(self, prices):
        # Hint: We want to find the maximum difference between two prices (buying price and selling price)
        i = 0  # Pointer for the buying price
        j = 1  # Pointer for the selling price
        max_profit = 0  # Initialize the maximum profit
        
        # Iterate through the prices array
        while j < len(prices):
            # If the price at j is less than the price at i, update both pointers
            if prices[i] > prices[j]:
                i += 1  # Move i to the next day
                j = i + 1  # Move j one step ahead of i
            else:
                # Calculate the profit if we sell at j and update max_profit if necessary
                max_profit = max(max_profit, prices[j] - prices[i])
                j += 1  # Move j to the next day
            
        return max_profit
