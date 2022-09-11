class Solution:
    def titleToNumber(self, c: str) -> int:
        Answer = 0
        for s in c:
            Answer = Answer*26 + ord(s)-ord('A')+1
        return Answer