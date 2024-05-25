class Solution(object):
    def lengthOfLongestSubstring(self, s):

        # Hint 1: What data structure can you use to quickly check if a character is repeated within a current window of characters?
        # Hint 2: How can removing characters from the start of a substring help you handle duplicates efficiently?

        charSet = set()  # Set to store unique characters
        left = 0  # Left pointer for the sliding window
        right = 0  # Right pointer for the sliding window
        max_length = 0  # Variable to keep track of the maximum length of the substring

        while right < len(s):
            letter = s[right]  # Current character

            if letter not in charSet:
                # If the character is not in the set, add it and update the max length
                charSet.add(letter)
                max_length = max(max_length, right - left + 1)
                right += 1
            else: 
                # If the character is in the set, remove the leftmost character and move the left pointer
                charSet.remove(s[left])
                left += 1

        return max_length