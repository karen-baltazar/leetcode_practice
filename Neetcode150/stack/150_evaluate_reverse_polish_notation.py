import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = [] 
        operations = set("+-*/")

        for t in tokens:
            if t in operations:
                # Perform the operation based on the token
                match t:
                    case '+':
                        op = result[-2] + result[-1]  
                    case '-':
                        op = result[-2] - result[-1]  
                    case '*':
                        op = result[-2] * result[-1]  
                    case '/':
                        op = math.trunc(result[-2] / result[-1])
                del result[-2:]
                result.append(op)
            else:
                result.append(int(t))

        return result[0]
