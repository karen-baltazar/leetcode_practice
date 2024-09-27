from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, curr = [], []  # res stores all partitions, curr stores the current partition
        n = len(s)

        def is_palindrome(s, l, r):
            # Check if substring s[l:r+1] is a palindrome
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i):
            # If we've checked the whole string, add the current partition
            if i == n:
                res.append(curr[:])  # Append a copy of the current partition
                return

            for j in range(i, n):
                # If substring s[i:j+1] is a palindrome, add it to the current partition
                if is_palindrome(s, i, j):
                    curr.append(s[i:j+1])
                    backtrack(j + 1)  # Recursively partition the rest
                    curr.pop()  # Backtrack to explore other partitions

        backtrack(0)
        return res
