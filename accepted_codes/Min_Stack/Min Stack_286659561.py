class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minVal = float('inf')

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minVal = min(self.minVal,x)

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp == self.minVal:
            if len(self.stack) > 0:
                self.minVal = min(self.stack)
            else:
                self.minVal = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
