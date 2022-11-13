class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(int(stack[-1])*2)
            elif op == "+":
                new = int(stack[-1]) + int(stack[-2])
                stack.append(new)
            else:
                stack.append(int(op))
        print(stack)
        return sum(stack)
                
                