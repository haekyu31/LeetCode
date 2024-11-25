class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        res = [i[0] for i in words]
        return "".join(res) == s