class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, comb = [], []

        def backtrack(start):
            # If the current combination reaches the desired size, add it to the result
            if len(comb) == k:
                res.append(comb[:])
                return

            # Iterate over the numbers starting from 'start' to 'n'
            for num in range(start, n + 1):
                comb.append(num)  # Add the current number to the combination
                backtrack(num + 1)  # Recursively build the next part of the combination
                comb.pop()  # Remove the last number to explore new combinations

        backtrack(1)  # Start building combinations from number 1
        return res
