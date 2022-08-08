class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        Me = []
        while len(piles)>0:
            A = [piles.pop()]
            Me.append(piles.pop())
            B = [piles.pop(0)]
        return sum(Me)