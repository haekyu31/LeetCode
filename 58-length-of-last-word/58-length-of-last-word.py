class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        S = s.split()
        return(len(S[-1]))