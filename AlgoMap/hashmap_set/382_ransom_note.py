class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Convert magazine to a hashmap, counting frequency of each character
        counter = defaultdict(int)
        for m in magazine:
            counter[m] += 1
            
        # Check that each character in ransomNote can be constructed from magazine
        for r in ransomNote:
            if r not in counter:  # If the character is not in the magazine
                return False
            elif counter[r] == 1:  # If the character is used up, remove it from the hashmap
                del counter[r]
            else:
                counter[r] -= 1  # Reduce the count of the character

        return True
