class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split("\n")
        stack = [] # [level, cum_size]
        ans = 0
        for line in lines:
            if not stack:
                level = line.count("\t")
                stack.append([level, len(line) - level])
                
            else:
                level = line.count("\t")
                while stack and stack[-1][0] >= level:
                    stack.pop()
                    
                offset = stack[-1][1] + 1 if stack else 0
                stack.append([level, offset + len(line) - level])
            
            if "." in line:
                ans = max(ans, stack[-1][1])
                
        return ans