class MinStack:

    def __init__(self):
        self.s = []
        self.minVal = float("inf")

    def push(self, val: int) -> None:
        self.s.append([val, min(val, self.minVal)])
        self.minVal = min(self.minVal, val)

    def pop(self) -> None:
        self.s.pop()
        if self.s:
            self.minVal = self.s[-1][1]
        else:
            self.minVal = float("inf")

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
