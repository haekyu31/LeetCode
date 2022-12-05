class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_heights = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if sort_heights[i] != heights[i]:
                res += 1
        return res