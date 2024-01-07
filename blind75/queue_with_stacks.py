class MyQueue:
    def __init__(self):
        self.stack = []
        self.reversed_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        out = None
        while self.stack:
            self.reversed_stack.append(self.stack.pop())
        out = self.reversed_stack.pop()
        while self.reversed_stack:
            self.stack.append(self.reversed_stack.pop())
        return out
        
    def peek(self) -> int:
        out = None
        while self.stack:
            self.reversed_stack.append(self.stack.pop())
        out = self.reversed_stack[-1]
        while self.reversed_stack:
            self.stack.append(self.reversed_stack.pop())
        return out

    def empty(self) -> bool:
        if len(self.stack) == 0 and len(self.reversed_stack) == 0:
            return True
        else:
            return False