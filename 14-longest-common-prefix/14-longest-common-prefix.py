class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0 :
            return ""   # 글자가 없는 경우
        if n == 1:      # 글자가 하나인 경우
            return strs[0]
        strs.sort()
        end = min(len(strs[0]), len(strs[n - 1]))
        i = 0
        while (i < end and
               strs[0][i] == strs[n - 1][i]):
            i += 1
        pre = strs[0][0: i]
        return pre        