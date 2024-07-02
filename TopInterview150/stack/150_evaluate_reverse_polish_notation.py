class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):  # Check if token is a number
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Perform integer division
                    if a * b < 0 and a % b != 0:
                        stack.append(a // b + 1)  # Adjust for negative results
                    else:
                        stack.append(a // b)

        return stack[-1]