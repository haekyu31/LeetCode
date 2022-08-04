class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # i_list = [i for i, nums in enumerate(nums)]
        # j_list = [j for j, nums in enumerate(nums)]
        # count = 0
        # for i in i_list:
        #     for j in j_list:
        #         if nums[i] == nums[j] and i < j:
        #             count += 1
        # return count        
        
        
                # 모든 digit에 대한 count를 구한다.
        Counts = collections.Counter(nums)
        # count가 2개 이상인 경우에 대해서 nC2 (pair의 수)를 Answer에 더한다
        Answer = 0
        for key, value in Counts.items():
            if value > 1:
                Answer += value * (value-1) / 2 # nC2
        return int(Answer)