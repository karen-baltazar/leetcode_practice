class Solution(object):
    def isPalindrome(self, s):
        # Hint: Utilize two pointers to compare characters from both ends
        # Filter out non-alphanumeric characters and convert to lowercase
        f = filter(unicode.isalnum, s.lower())
        s1 = "".join(f)
        
        i = 0
        j = len(s1) - 1
        
        # Compare characters from both ends towards the middle
        while i <= j:
            if s1[i] != s1[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
