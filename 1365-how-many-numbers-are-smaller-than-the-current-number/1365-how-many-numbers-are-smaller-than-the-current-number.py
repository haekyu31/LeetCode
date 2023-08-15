class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=[]
        numi = sorted(nums)
        for i in range(0,len(nums)):
            a.append(numi.index(nums[i]))
        return a