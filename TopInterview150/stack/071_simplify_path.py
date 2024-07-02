class Solution(object):
    def simplifyPath(self, path):
        # Stack to keep track of the valid directories
        stack = []
        # Variable to build the current directory name
        directory = ""

        # Iterate through each character in the path
        for char in path + "/":
            if char == "/":
                # When encountering a slash, process the built directory name
                if directory == "..":
                    # If directory is '..', pop from stack if not empty
                    if stack:
                        stack.pop()
                elif directory != "" and directory != ".":
                    # If directory is valid (not empty or '.'), push to stack
                    stack.append(directory)
                # Reset the directory name
                directory = ""
            else:
                # Continue building the directory name
                directory += char

        # Build the simplified path manually
        simplified_path = "/"
        for i in range(len(stack)):
            simplified_path += stack[i]
            if i < len(stack) - 1:
                simplified_path += "/"
        
        return simplified_path
