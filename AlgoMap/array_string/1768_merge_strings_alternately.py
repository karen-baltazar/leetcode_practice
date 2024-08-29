class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Hint: Iterate through both strings simultaneously and append characters alternately.
        
        # Initialize an empty list to store the merged characters
        merged = []
        index = 0
        len1, len2 = len(word1), len(word2)

        # Iterate while there are characters in both strings
        while index < len1 and index < len2:
            # Add characters from both strings alternately
            merged.append(word1[index])
            merged.append(word2[index])
            index += 1

        # Append the remaining characters from word1 if any
        if index < len1:
            merged.extend(word1[index:])

        # Append the remaining characters from word2 if any
        if index < len2:
            merged.extend(word2[index:])

        # Join the list of characters into a single string and return it
        return ''.join(merged)
