class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        string = ""
        for i in num:
            string += str(i)
        Answer = int(string) + k
        return str(Answer)