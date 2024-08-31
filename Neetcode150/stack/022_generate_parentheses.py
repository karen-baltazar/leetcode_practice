class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        def backtrack(open_count: int, close_count: int) -> None:
            # If we have used all open and close parentheses, add the current combination to the result
            if open_count == close_count == n:
                result.append("".join(path))
                return
            
            # If we can still add an open parenthesis, do so
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count) # Recursively add more parentheses
                path.pop()  # Backtrack by removing the last added parenthesis

            # If we can add a close parenthesis, do so
            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1)
                path.pop()

        backtrack(0, 0)
        return result
