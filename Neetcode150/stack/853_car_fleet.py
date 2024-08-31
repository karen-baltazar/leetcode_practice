class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Hint: Consider the time it takes for each car to reach the target 
        # and how cars might form groups (fleets) if one catches up to another.
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s)

            # If the current car catches up to the car in front, they form a fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
