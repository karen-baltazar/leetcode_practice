class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start <= end:
            while start < end and not s[start].isalnum():
                start += 1  # Skip non-alphanumeric characters from the start

            while start < end and not s[end].isalnum():
                end -= 1  # Skip non-alphanumeric characters from the end

            if s[start].lower() != s[end].lower():
                return False  # Characters do not match

            start += 1
            end -= 1 

        return True  