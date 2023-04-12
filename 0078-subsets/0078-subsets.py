class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(res, 0, [], nums)
        return res
    
    def dfs(self, res:list, start:int, subset:int, nums:list):
        res.append(list(subset))
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.dfs(res, i+1, subset, nums)
            subset.pop()