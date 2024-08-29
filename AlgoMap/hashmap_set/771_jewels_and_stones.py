class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Convert 'jewels' to a set for O(1) lookups
        jset = set(jewels)

        # Count how many stones are jewels
        count = 0
        for s in stones:
            if s in jset:
                count += 1

        return count
