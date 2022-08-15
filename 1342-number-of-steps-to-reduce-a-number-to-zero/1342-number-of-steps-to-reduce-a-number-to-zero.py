class Solution:
    def numberOfSteps(self, num: int) -> int:
        CurrentNum = num
        nCount = 0
        while CurrentNum != 0:
            if CurrentNum % 2 == 0:
                CurrentNum /= 2
            else:
                CurrentNum -= 1
            nCount += 1
        return nCount
