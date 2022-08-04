class Solution:
    def findGCD(self, nums: List[int]) -> int:
        Max = max(nums)
        Min = min(nums)
        return gcd(Max, Min)
        
        
        #gcd func
        # def gcd(x, y):
        #     if x % y==0:
        #         return y
        #     return gcd(y, x%y)
        # # if Max%Min ==0 :
        #     return Min
        # else:
        #     Max = Max%%