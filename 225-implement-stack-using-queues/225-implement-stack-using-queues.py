class MyStack:

    def __init__(self):
        self.Stack1 = []
    def push(self, x: int) -> None:
        self.Stack1.append(x)
        print(self.Stack1)
    def pop(self) -> int:
        while len(self.Stack1)>0:
            return self.Stack1.pop()
    def top(self) -> int:
        return self.Stack1[-1]

    def empty(self) -> bool:
        print(self.Stack1)
        return len(self.Stack1) ==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()