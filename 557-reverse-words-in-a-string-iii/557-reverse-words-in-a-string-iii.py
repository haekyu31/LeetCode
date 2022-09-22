class Solution:
    def reverseWords(self, s: str) -> str:
        res = [i[::-1] for i in s.split()]
        Answer = ""
        for i in res:
            Answer += i+" "
        return Answer[:-1]
        # return " ".join([i[::-1] for i in s.split()])