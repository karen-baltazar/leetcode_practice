class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        char_count = [0] * 26 # Array to count the frequency of each character in the current window

        for right in range(len(s)):
            char_count[ord(s[right]) - 65] += 1

            # Check if the current window is valid.
            # A window is valid if the number of characters to replace does not exceed 'k'
            while (right - left + 1) - max(char_count) > k:
                # If the window is not valid, move the left pointer to reduce the window size
                char_count[ord(s[left]) - 65] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
