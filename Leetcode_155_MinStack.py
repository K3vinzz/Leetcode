class MinStack:
    items = []
    minList = []
    def push(self, val: int) -> None:
        self.items.append(val)
        if len(self.items) == 1:
            self.minList.append(val)
        else:
            if val < self.minList[-1]:
                self.minList.append(val)
            else:
                self.minList.append(self.minList[-1])

    def pop(self) -> None:
        self.items.pop()
        self.minList.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minList[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-1)
# obj.pop()
print(obj.top())
print(obj.getMin())