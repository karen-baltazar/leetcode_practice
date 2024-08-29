class Solution:
    def reverseString(self, s: List[str]) -> None:
        start, end = 0, len(s) - 1 

        # Swap characters until the pointers meet in the middle
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1 
