class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        minVal = min(self.getMin(),x)
        self.stack.append((x,minVal))

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][0]
        return -1

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][1]
        return float('inf')


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
