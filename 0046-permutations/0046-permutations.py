class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(nums, perm=[], res=[]):
            if not nums:
                res.append(perm[::])
            
            for i in range(len(nums)):
                new_nums = nums[:i] + nums[i+1:]
                perm.append(nums[i])
                recursive(new_nums, perm, res)
                perm.pop()
            return res
        return recursive(nums)