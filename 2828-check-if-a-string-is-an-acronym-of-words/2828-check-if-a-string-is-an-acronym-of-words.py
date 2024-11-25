class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res = []
        for i in words:
            res.append(i[0])
        return "".join(res) == s