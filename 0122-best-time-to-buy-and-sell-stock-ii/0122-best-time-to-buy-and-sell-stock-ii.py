class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0보다 크면 무조건 합산
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices) -1 ))
        # res = 0
        # # 값이 오를때 마다 그리디 계산
        # for index in range(len(prices)-1):
        #     if prices[index + 1] > prices[index]:
        #         res += prices[index + 1] - prices[index]
        # return res