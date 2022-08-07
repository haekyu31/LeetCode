class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Answer = []
        # for i in range(len(nums)):
        #     s = 0
        #     for j in range(i+1):
        #         s += nums[j]
        #     Answer.append(s)
        # return Answer
        curentSum = 0
        sum_list = []
        for i in range(len(nums)):
            curentSum += nums[i]
            sum_list.append(curentSum)
        return sum_list
            