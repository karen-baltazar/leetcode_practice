class Solution(object):
    def maxArea(self, height):
        # Hint: Adjust pointers based on the minimum height to maximize area.
        # Initialize maximum area and pointers
        max_area = 0
        i = 0
        j = len(height) - 1

        # Continue until the two pointers meet
        while i < j:
            # Calculate current area and update maximum area
            curr_area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, curr_area)

            # Move pointer with the smaller height towards the center
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
