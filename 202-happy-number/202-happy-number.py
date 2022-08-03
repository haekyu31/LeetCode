class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_n(n):
            sum_n = 0
            while n//1 !=0:
                sum_n += (n%10)**2
                n = int(n/10)
            return sum_n
        
        while True:
            n = sum_n(n)
            if n == 4:
                return False
                break
            elif n == 1:
                return True
                break