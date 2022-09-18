class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # result = 0
        # for x in nums:
        #     if x-diff in nums and x+diff in nums:
        #         result += 1
        # return result
        cnt = 0
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                diff1 = nums[j] - nums[i]
                diff2 = nums[k] - nums[j]
                if diff1 == diff:
                    if diff2 == diff:
                        cnt +=1
                        j +=1
                    else: k -=1
                else:
                    j+=1
        return cnt