class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(e for e in s if e.isalnum())    # 문장부호 제거
        s_low = s.lower()                           # 소문자로 만들기
        s_reverse = s_low[::-1]                     # 문자열 뒤집기
        if s_low == s_reverse:                      # 뒤집은 문자열 비교
            return True
        else:
            return False
