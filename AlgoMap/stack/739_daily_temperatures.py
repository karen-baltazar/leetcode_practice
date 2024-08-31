class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Hint: Use a stack to track previous temperatures and their indices to find the next warmer day.
        days_to_wait = [0] * len(temperatures)
        stack = []

        for i, current_temp in enumerate(temperatures):
            while stack and stack[-1][0] < current_temp:
                prev_temp, prev_index = stack.pop()
                days_to_wait[prev_index] = i - prev_index
            
            stack.append([current_temp, i])

        return days_to_wait
