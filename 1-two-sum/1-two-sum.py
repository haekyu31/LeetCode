class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in ans:
                return[ans[m], i]
            else :
                ans[n] = i