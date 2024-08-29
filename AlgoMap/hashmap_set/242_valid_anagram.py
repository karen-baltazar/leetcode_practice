class Solution(object):
    def isAnagram(self, s, t):
        # An anagram has the exact same character counts for each letter.

        # If the lengths are not the same, the strings can't be anagrams
        if len(s) != len(t):
            return False

        # Dictionaries to store the frequency of characters in both strings
        countS, countT = {}, {}

        # Iterate over the strings and fill the dictionaries
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)  # Increase character count for s
            countT[t[i]] = 1 + countT.get(t[i], 0)  # Increase character count for t

        # If both dictionaries have the same frequencies, the strings are anagrams
        return countS == countT
