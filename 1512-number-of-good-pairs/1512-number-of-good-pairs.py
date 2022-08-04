class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        i_list = [i for i, nums in enumerate(nums)]
        j_list = [j for j, nums in enumerate(nums)]
        count = 0
        for i in i_list:
            for j in j_list:
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count        