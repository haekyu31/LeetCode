class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for index in range(len(nums)):
            if nums[index] != 0 :
                nums[i], nums[index] = nums[index], nums[i]
                i += 1
            