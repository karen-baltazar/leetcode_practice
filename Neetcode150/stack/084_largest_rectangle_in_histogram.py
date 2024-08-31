class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # Stack to store pairs of (index, height)
        heights.append(0)  # Add a zero height to ensure all bars are processed

        for i, current_height in enumerate(heights):
            start_index = i

            while stack and stack[-1][1] > current_height:
                prev_index, prev_height = stack.pop()
                max_area = max(max_area, prev_height * (i - prev_index))
                start_index = prev_index

            stack.append((start_index, current_height))
        
        return max_area