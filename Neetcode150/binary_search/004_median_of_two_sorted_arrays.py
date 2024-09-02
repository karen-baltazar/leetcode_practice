from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Hint: Use binary search on the smaller array to find the correct partition
        such that all elements on the left of the partition are less than or equal 
        to all elements on the right.
        """

        # Assign the smaller array to A and the larger to B
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total_len = len(A) + len(B)  # Total length of both arrays
        half = total_len // 2  # Halfway point

        l, r = 0, len(A) - 1  # Binary search bounds

        while True:
            i = (l + r) // 2  # Midpoint in A
            j = half - i - 2  # Complementary index in B

            # Get left and right elements around the partition in A
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')

            # Get left and right elements around the partition in B
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            # Check if the partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # If odd total length, return the middle element
                if total_len % 2:
                    return min(Aright, Bright)
                # If even, return the average of the two middle elements
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # Adjust the binary search range
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
