class Solution(object):
    def isSubsequence(self, s, t):
        # Hint: Track character positions for matching substrings
        if len(s) == 0:
            return True

        if len(t) == 0:
            return False

        i = 0
        for char in t:
            if char == s[i]:
                i += 1

            if i == len(s):
                return True

        return False
