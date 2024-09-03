class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Initialize frequency arrays for characters in 's1' and the sliding window in 's2'
        s1_freq = [0] * 26
        window_freq = [0] * 26
        len_s1, len_s2 = len(s1), len(s2)
        left = 0

        # If 's1' is longer than 's2', 's1' cannot be a permutation of any substring of 's2'
        if len_s1 > len_s2:
            return False

        # Populate frequency array for 's1'
        for char in s1:
            s1_freq[ord(char) - ord('a')] += 1

        # Initialize the frequency array for the first window of size 'len_s1' in 's2'
        for i in range(len_s1):
            window_freq[ord(s2[i]) - ord('a')] += 1

        # Check if the initial window is a permutation of 's1'
        if s1_freq == window_freq:
            return True

        # Slide the window over 's2'
        for right in range(len_s1, len_s2):
            # Add the new character from the right end of the window
            window_freq[ord(s2[right]) - ord('a')] += 1
            # Remove the character that is sliding out from the left end of the window
            window_freq[ord(s2[left]) - ord('a')] -= 1
            left += 1
            
            # Check if the current window is a permutation of 's1'
            if s1_freq == window_freq:
                return True

        return False
