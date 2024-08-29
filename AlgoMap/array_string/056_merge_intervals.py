class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Hint: Think about how to merge overlapping intervals by sorting them first.

        intervals.sort(key=lambda interval: interval[0])  # Sort intervals by the start time
        merged = []

        for interval in intervals:
            # If no overlap, add the current interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # If there is overlap, merge the current interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
