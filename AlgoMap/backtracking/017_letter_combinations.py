class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Map from digits to corresponding letters
        digit_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        # Result list for combinations and a temporary string to build combinations
        combinations, temp = [], [""]
        n = len(digits)

        def backtrack(index):
            # Base case: when the current index matches the length of digits
            if index == n:
                combinations.append(temp[0])  # Add the current combination
                return

            # Iterate over the letters corresponding to the current digit
            for letter in digit_map[digits[index]]:
                temp[0] += letter  # Add the current letter to the combination
                backtrack(index + 1)  # Recur to the next digit
                temp[0] = temp[0][:-1]  # Remove the last letter for backtracking

        if digits:  # Only start backtracking if digits is not empty
            backtrack(0)
        
        return combinations  # Return the complete list of combinations
