class Solution(object):
    def isSubsequence(self, s, t):
        # Hint: Use two pointers to check if s is a subsequence of t.
        
        # Edge case: if s is an empty string, it is a subsequence of any string
        if len(s) == 0:
            return True

        # Edge case: if t is an empty string and s is not, s cannot be a subsequence
        if len(t) == 0:
            return False

        i = 0  # Pointer for s
        # Iterate through t to find the characters of s
        for char in t:
            if char == s[i]:
                i += 1  # Move the pointer in s

            # If all characters in s have been matched
            if i == len(s):
                return True

        # If not all characters in s have been matched
        return False
