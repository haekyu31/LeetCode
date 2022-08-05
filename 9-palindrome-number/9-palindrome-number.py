class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        li = list(str(x))
        if li == li[::-1]:
            return True
        else: return False