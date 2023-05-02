class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = reduce(lambda x,y: x*y, nums)
        return 0 if not product else 1 if product >0 else -1