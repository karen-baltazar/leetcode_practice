class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Hint: Compare characters at each position to find the common prefix.
        
        min_length = float('inf')  # Minimum length among all strings
        i = 0  # Index to traverse characters

        # Find the minimum length among all strings
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        # Iterate over characters up to the minimum length
        while i < min_length:
            for s in strs:
                # Compare the current character with the one in the first string
                if s[i] != strs[0][i]:
                    return strs[0][:i]  # Return the common prefix found
            i += 1  # Move to the next character

        return strs[0][:i]  # Return the common prefix if all characters are traversed
