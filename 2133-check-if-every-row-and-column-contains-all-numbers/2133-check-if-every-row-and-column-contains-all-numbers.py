class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        set_ = set(range(1, len(matrix)+1))
        return all(set_ == set(x) for x in matrix+list(zip(*matrix)))