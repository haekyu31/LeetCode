class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0 :
        #     return False
        # li = list(str(x))
        # if li == li[::-1]:
        #     return True
        # else: return False
        if x < 0 :
            return False
        reverse = 0
        X = x
        while x:
            reverse =reverse *10 + (x%10)
            x //= 10
        return reverse == X