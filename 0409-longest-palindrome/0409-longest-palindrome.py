class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 홀수인지 확인용, 홀수라면 -1 을하고 마지막에 1을 더해주는 식
        odd = False

        count = collections.Counter(s)
        res = 0
        
        for value in count.values():
            if value % 2 ==1:
                res += value -1
                odd = True
            else:
                res += value
        if odd == True:
            return res + 1
        return res
                