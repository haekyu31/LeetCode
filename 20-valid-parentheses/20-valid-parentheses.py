class Solution:
    def isValid(self, s: str) -> bool:
        InputList = list(s)
        
        Stack = []
        
        for input in InputList:
            if input in ['(', '{','[']:
                Stack.append(input)
            else:
                if len(Stack) == 0:
                    return False
                if Stack[-1] == '(' and input == ')':
                    Stack.pop()
                elif Stack[-1] == '{' and input == '}':
                    Stack.pop()
                elif Stack[-1] == '[' and input == ']':
                    Stack.pop()
                else:
                    return False
        if len(Stack)>0:
            return False
        return True
            