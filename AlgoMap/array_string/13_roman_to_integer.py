class Solution:
    def romanToInt(self, s: str) -> int:
        # Hint: Use a dictionary to map Roman numerals to integers and process the string to handle subtractive cases.
        
        # Dictionary to map Roman numerals to their integer values
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        integer = 0  # Variable to store the resulting integer value
        i = 0  # Index to iterate through the string
        n = len(s)  # Length of the input string

        # Iterate through the string
        while i < n:
            # Check if the current numeral is less than the next numeral (subtractive case)
            if i < n - 1 and roman[s[i]] < roman[s[i + 1]]:
                integer += roman[s[i + 1]] - roman[s[i]]
                i += 2  # Move past the next numeral
            else:
                integer += roman[s[i]]
                i += 1  # Move to the next numeral

        return integer
