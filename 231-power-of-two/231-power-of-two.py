class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = 0
        while True:
            if 2**num <n :
                num += 1
            elif 2**num>n:
                return False
            else :
                return True
