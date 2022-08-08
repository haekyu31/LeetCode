class Solution:
    def minimumSum(self, num: int) -> int:
        #Greedy Algorithm
        
        numlist = [int(i) for i in list(str(num))]
        numlist.sort()
        digits_10 = sum(numlist[0:2])*10
        digits_1 = sum(numlist[2:])
        return digits_10 + digits_1