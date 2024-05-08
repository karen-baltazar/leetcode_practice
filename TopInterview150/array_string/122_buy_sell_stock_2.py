class Solution(object):
    def maxProfit(self, prices):
        # Hint: Visualize the stock prices as a graph. Look for local minima and maxima to determine profitable transactions.
        
        i = 0  # Pointer for the buying price
        j = 1  # Pointer for the selling price
        d = len(prices)
        max_profit = 0
        
        # Iterate through the prices array
        while j < d:
            # Check if it is a profitable transaction
            if prices[i] < prices[j]:
                if j == (d - 1) or ((j + 1) < d and prices[j] > prices[j + 1]):
                    # Update max_profit and move pointers
                    max_profit += prices[j] - prices[i]
                    j += 1
                    i = j
            else:
                # Move the buying pointer to the current day
                i = j
            # Move the selling pointer to the next day
            j += 1
        
        return max_profit
