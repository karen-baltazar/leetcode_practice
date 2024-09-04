class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: if t is empty, return an empty string
        if not t:
            return ""

        # Frequency dictionaries for characters in t and the current window in s
        t_freq, window_freq = {}, {}

        # Populate t_freq with the frequency of each character in t
        for char in t:
            t_freq[char] = 1 + t_freq.get(char, 0)

        have, need = 0, len(t_freq)
        result, min_length = [-1, -1], float('inf')
        left = 0

        # Iterate over the characters in s using the right pointer
        for right in range(len(s)):
            char = s[right]
            window_freq[char] = 1 + window_freq.get(char, 0)

            # If the current character in the window matches the frequency in t, increase `have`
            if char in t_freq and window_freq[char] == t_freq[char]:
                have += 1

            # When all needed characters are in the current window
            while have == need:
                # Update the result if the current window is smaller
                if (right - left + 1) < min_length:
                    result = [left, right]
                    min_length = (right - left + 1)

                # Move the left pointer to shrink the window
                window_freq[s[left]] -= 1
                if s[left] in t_freq and window_freq[s[left]] < t_freq[s[left]]:
                    have -= 1

                left += 1

        left, right = result
        # Return the minimum window substring or an empty string if no valid window was found
        return s[left:right + 1] if min_length != float('inf') else ""
