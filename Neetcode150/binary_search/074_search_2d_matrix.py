class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Define the left and right bounds for the binary search in the columns
        left, right = 0, len(matrix[0]) - 1
        
        # Iterate over each row to find the potential row where target might be
        for i, row in enumerate(matrix):
            # Check if the target is within the range of the current row
            if target >= row[0] and target <= row[right]:
                # Perform binary search in this row
                while left <= right:
                    mid = (left + right) // 2
                    if target == row[mid]:
                        return True
                    elif target > row[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                # Target not found in this row
                return False
        
        # Target not found in any row
        return False
