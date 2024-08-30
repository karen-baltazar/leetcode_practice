class Solution:
    def isValid(self, s: str) -> bool:
        # Hint: Use a stack to track open parentheses and match them with their corresponding closing parentheses.
        closed_open = {')': '(', '}' : '{', ']': '['}
        stack = []

        for bracket in s:
            if bracket in closed_open:
                if stack and stack[-1] == closed_open[bracket]:
                    prev = stack.pop()  # Remove matching opening bracket from stack
                else:
                    return False  # Unmatched closing bracket found
            else:
                stack.append(bracket)

        return True if not stack else False
