class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()  # Track characters currently in the substring
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Store the maximum length of the substring found

        for right in range(len(s)):  # Right pointer of the sliding window
            if s[right] not in seen_chars:
                seen_chars.add(s[right])
            else:
                while s[left] != s[right]:
                    seen_chars.remove(s[left])
                    left += 1
                left += 1
                
            max_length = max(max_length, right - left + 1)

        return max_length
