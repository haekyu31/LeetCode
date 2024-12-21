class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValid(segment):
            return len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255)
        
        def backtrack(start, path):
            if len(path) == 4:
                if start ==  len(s):
                    result.append('.'.join(path))
                return
            
            for length in range(1, 4):
                if start + length <= len(s):
                    segment = s[start:start + length]
                    if isValid(segment):
                        backtrack(start + length, path + [segment])
        
        result = []
        backtrack(0, [])
        
        return result