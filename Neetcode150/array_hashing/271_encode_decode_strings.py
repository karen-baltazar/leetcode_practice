class Solution:
    def encode(self, strs: List[str]) -> str:
        # Hint: Use a delimiter to separate the length of each string from the string itself.

        res = ""

        # Iterate through each string in the list
        for s in strs:
            # Append the length of the string, a delimiter, and the string itself
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        # Hint: Extract lengths and strings using the delimiter to reconstruct the original list.

        res, i = [], 0

        # Process the encoded string
        while i < len(s):
            # Find the delimiter to get the length of the next string
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            # Extract the string based on the length
            res.append(s[j + 1: j + 1 + length])
            # Move to the next encoded string
            i = j + 1 + length

        return res
