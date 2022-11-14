class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child_i = cookie_i = 0
        
        # 만족하지 못할 때 까지 그리디 진행
        while child_i < len(g) and cookie_i <len(s):
            if s[cookie_i] >= g[child_i]:
                child_i += 1
            cookie_i += 1
        return child_i