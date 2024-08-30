class Solution:
    def trap(self, height: List[int]) -> int:
        # Solution 1: Using auxiliary arrays (intuitive but uses more space)
        trap_water = 0
        
        # Maximum height to the left and right of each element
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        
        maxHeight = 0
        for i in range(len(height)):
            maxLeft[i] = maxHeight
            maxHeight = max(maxHeight, height[i])

        maxHeight = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = maxHeight
            maxHeight = max(maxHeight, height[i])

        # Calculate the water trapped above each element
        for i in range(len(height)):
            cur_water = min(maxLeft[i], maxRight[i]) - height[i]
            if cur_water > 0:
                trap_water += cur_water

        return trap_water

        # Solution 2: Two-pointer approach (less space but more complex)
        trap_water = 0
        left, right = 0, len(height) - 1
        
        # Maximum heights encountered from the left and right
        maxLeft = height[left]
        maxRight = height[right]

        while left < right:
            # If the left max is smaller or equal, process the left pointer
            if maxLeft <= maxRight:
                trap_water += max(0, maxLeft - height[left])
                left += 1
                maxLeft = max(maxLeft, height[left])
            # Otherwise, process the right pointer
            else:
                trap_water += max(0, maxRight - height[right])
                right -= 1
                maxRight = max(maxRight, height[right])
        
        return trap_water
