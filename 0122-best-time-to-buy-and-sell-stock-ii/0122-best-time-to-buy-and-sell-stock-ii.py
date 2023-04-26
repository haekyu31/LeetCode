class Solution:
    def maxProfit(self, price: List[int]) -> int:
        result = 0
        for i in range(len(price) -1):
            if price[i+1] > price[i]:
                result += price[i+1] - price[i]
        return result