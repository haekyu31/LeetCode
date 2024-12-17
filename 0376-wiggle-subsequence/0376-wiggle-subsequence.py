class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        peak = valley = 0
        for i in range(1, len(nums)):
            # current element could be a peak
            if nums[i - 1] < nums[i]:
                peak = valley + 1
            # current element could be a valley
            elif nums[i - 1] > nums[i]:
                valley = peak + 1
        # add 1 because we didn't count the first element
        return 1 + max(peak, valley)