class Solution:
    def checkPalindrome(self, s: str) -> bool:
        s_reverse = s[::-1]
        return s == s_reverse    
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            if self.checkPalindrome(s) :
                return s
        return ""