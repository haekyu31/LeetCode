class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es = sum(nums)
        dg=0
        for x in nums:
            while x>0:
                dg+=(x%10)
                x=x//10
        return abs(es-dg)