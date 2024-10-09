class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev, cur = 0, 0  # Initialize the cost for the first two steps (starting point).

        # Iterate from the third step to the top (n + 1 to account for reaching the top).
        for i in range(2, n + 1):
            # For each step, calculate the minimum cost by considering the two possible
            # previous steps and adding their respective costs.
            prev, cur = cur, min(cost[i - 2] + prev, cost[i - 1] + cur)

        return cur  # Return the minimum cost to reach the top.
