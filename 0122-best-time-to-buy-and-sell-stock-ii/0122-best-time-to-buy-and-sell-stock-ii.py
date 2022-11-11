class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        # 값이 오를때 마다 그리디 계산
        for index in range(len(prices)-1):
            if prices[index + 1] > prices[index]:
                res += prices[index + 1] - prices[index]
        return res