class Solution(object):
    def isValid(self, s):
        # Stack to keep track of opening brackets
        stack = []
        # Dictionary to map closing brackets to their corresponding opening brackets
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}

        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in closeToOpen:
                # Check if the stack is not empty and the top of the stack matches the corresponding opening bracket
                if stack and stack[-1] == closeToOpen[char]:
                    # Pop the opening bracket from the stack
                    stack.pop()
                else:
                    # If not, the string is not valid
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets are matched correctly
        return True if not stack else False
