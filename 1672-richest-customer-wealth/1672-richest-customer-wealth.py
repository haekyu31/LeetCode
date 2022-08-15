class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

#         sum_i = []
#         for i in accounts:
#             sum_i.append(sum(i))
#         mx = max(sum_i)    
#         return mx    

        # Max = 0 
        # for i in range(len(accounts)):
        #     CurrentSum = 0
        #     for j in range(len(accounts[i])):
        #         CurrentSum += accounts[i][j]
        #     if Max < CurrentSum:
        #         Max = CurrentSum
        # return Max
        
        Max = 0
        for i in accounts:
            if Max < sum(i):
                Max = sum(i)
        return Max