class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0 :
            return ""   # 글자가 없는 경우
        if n == 1:      # 글자가 하나인 경우
            return strs[0]
        strs.sort()     # 단어를 알파벳 순으로 정렬
        end = min(len(strs[0]), len(strs[n - 1]))  # 가장 첫번째와 가장 마지막단어의 길이중 짧은것을 선택
        i = 0
        while (i < end and
               strs[0][i] == strs[n - 1][i]):    # 정렬된 첫번째 단어와 마지막 단어를  짧은 길이까지 확인
            i += 1
        pre = strs[0][0: i]
        return pre        