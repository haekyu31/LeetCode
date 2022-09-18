class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        result = 0
        for x in nums:
            if x-diff in nums and x+diff in nums:
                result += 1
        return result