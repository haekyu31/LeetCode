class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         strings = list(s)
        
#         for i in strings:
#             if i in ['(', '{', '[']:
#                 stack.append(i)
#             else:
#                 if len(stack) ==0:
#                     return False
#                 if stack[-1] =='(' and i == ')':
#                     stack.pop()
#                 elif stack[-1] =='{' and i == '}':
#                     stack.pop()
#                 elif stack[-1] =='[' and i == ']':
#                     stack.pop()
#                 else:
#                     return False
#         if len(stack)>0:
#             return False
#         return True
    
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []