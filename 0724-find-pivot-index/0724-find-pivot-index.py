class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left = 0
        sum_right = sum(nums)
        
        for i in range(len(nums)):
            sum_right -= nums[i]
            if sum_left == sum_right:
                return i
            sum_left += nums[i]
        return -1