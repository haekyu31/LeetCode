class Solution:
    def addDigits(self, num: int) -> int:
        
        

        nums = [int(i) for i in list(str(num))]
        ans = 0

        for i in nums:
            ans += i
            print(ans)
        if ans < 10:
            return ans
        else:
            return self.addDigits(ans)

