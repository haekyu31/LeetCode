class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hset = {}
        s_list = s.split()
        if len(pattern) != len(s_list) or len(set(pattern)) != len(set(s_list)): return False # 예외조건
        for index, char in enumerate(pattern):
            if char in hset:
                if hset[char] != s_list[index]:
                    return False
            else: 
                hset[char] = s_list[index]
        return True
