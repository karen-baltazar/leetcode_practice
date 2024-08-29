class Solution(object):
    def rotate(self, matrix):
        left, right = 0, len(matrix) - 1  # Initialize pointers to the boundaries of the matrix

        while left < right:
            # Rotate the elements in the current boundary
            for i in range(right - left):
                top, bottom = left, right  # Define the current top and bottom rows

                # Save the top left element
                topLeft = matrix[top][left + i]

                # Move the bottom left element to the top left position
                matrix[top][left + i] = matrix[bottom - i][left]

                # Move the bottom right element to the bottom left position
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Move the top right element to the bottom right position
                matrix[bottom][right - i] = matrix[top + i][right]

                # Move the saved top left element to the top right position
                matrix[top + i][right] = topLeft

            # Move the boundaries inward
            right -= 1
            left += 1


# Note: The variable 'i' is crucial for managing the rotation of elements within the current boundary.
# It acts as an offset that helps to access elements not directly on the boundary lines but within
# the submatrix defined by the current left, right, top, and bottom boundaries. By incrementing 'i',
# we can correctly shift each element to its new position during the 90-degree rotation.
