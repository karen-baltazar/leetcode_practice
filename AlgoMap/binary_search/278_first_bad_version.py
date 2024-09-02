# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Hint: Use binary search to find the first bad version efficiently. 
        # Consider how to minimize the number of API calls.

        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                # Check if it's the first bad version
                if not isBadVersion(mid - 1):
                    return mid 
                else:
                    high = mid - 1
            else:
                low = mid + 1

