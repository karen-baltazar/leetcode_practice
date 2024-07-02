class MinStack(object):

    # Hint: Consider using an auxiliary stack to keep track of the minimum values.

    def __init__(self):
        # Initialize two stacks: one for all values and one for minimum values
        self.stack = []
        self.minStack = []

    def push(self, val):
        # Push the value onto the main stack
        self.stack.append(val)
        # Push the minimum value onto the minStack
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self):
        # Pop the value from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        # Return the top value from the main stack
        return self.stack[-1]
        
    def getMin(self):
        # Return the top value from the minStack, which is the minimum value
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
