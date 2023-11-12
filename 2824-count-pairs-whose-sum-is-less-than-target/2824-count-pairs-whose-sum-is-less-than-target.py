class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        left = 0
        right = len(nums)-1
        while(left < right):
            if(nums[left] + nums[right] < target):
                count = count + (right - left)
                left = left + 1
            else:
                right = right - 1
        return count