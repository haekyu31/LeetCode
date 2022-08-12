class MyQueue:

    def __init__(self): # 빈 리스트를 만들어서 큐 스택을 사용하기
        self.Stack1 = []
        self.Stack2 = []

    def push(self, x: int) -> None:
        self.Stack1.append(x)  #큐에 집어넣기

    def pop(self) -> int:
        while len(self.Stack1)>0:
            self.Stack2.append(self.Stack1.pop())
        Answer = self.Stack2.pop()
        while len(self.Stack2)>0:
            self.Stack1.append(self.Stack2.pop())
        return Answer
        
    def peek(self) -> int:
        while len(self.Stack1)>0:
            self.Stack2.append(self.Stack1.pop())
        Answer = self.Stack2[-1]
        while len(self.Stack2)>0:
            self.Stack1.append(self.Stack2.pop())
        return Answer
        

    def empty(self) -> bool:
        return len(self.Stack1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



# class MyQueue:
#     def __init__(self):
#         self.Stack1 = []
#         self.Stack2 = []
#     def push(self, x: int) -> None:
#         self.Stack1.append(x)
#     def pop(self) -> int:
#         # Stack1에서 pop하여 Stack2에 쌓기 (뒤집어서 들어감)
#         while len(self.Stack1) > 0:
#             self.Stack2.append(self.Stack1.pop())
#         returnValue = self.Stack2.pop()
#         while len(self.Stack2) > 0:
#             self.Stack1.append(self.Stack2.pop())
#         return returnValue
#     def peek(self) -> int:
#         while len(self.Stack1) > 0:
#             self.Stack2.append(self.Stack1.pop())
#         returnValue = self.Stack2[ len(self.Stack2) -1 ]
#         while len(self.Stack2) > 0:
#             self.Stack1.append(self.Stack2.pop())
#         return returnValue
#     def empty(self) -> bool:
#         return len(self.Stack1) == 0