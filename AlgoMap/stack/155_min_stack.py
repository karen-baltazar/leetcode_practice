class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = [] 

    def push(self, value: int) -> None:
        self.main_stack.append(value) 
        min_value = self.min_stack[-1] if self.min_stack else value

        if value <= min_value:
            self.min_stack.append(value)

    def pop(self) -> None:
        top_value = self.main_stack.pop() 

        if top_value == self.min_stack[-1]:
            self.min_stack.pop() 
        
    def top(self) -> int:
        return self.main_stack[-1]  
        
    def getMin(self) -> int:
        return self.min_stack[-1]  
        