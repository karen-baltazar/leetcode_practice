class Solution(object):
    def groupAnagrams(self, strs):
        # Hint: Use a hashmap (dictionary) to group anagrams based on character counts.
        
        # Create a dictionary to group words by their sorted character representation
        groups = defaultdict(list)

        for word in strs:
            # Convert each word to a tuple of character counts (hashable key)
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1
            
            key = tuple(count)
            groups[key].append(word)

        return list(groups.values())
