class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Hint: Use binary search to efficiently determine if a number is a perfect square by narrowing down the possible candidates.
        left, right = 1, num

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True
            elif square > num:
                right = mid - 1 
            else:
                left = mid + 1

        return False  # No perfect square found