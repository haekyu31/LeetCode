class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left,right + 1):
            a = bin(i)[2:]
            t = a.count("1")
            l = []
            if t==1:
                pass
            else:
                for i in range(2,t):
                    if t%i==0:
                        break
                else:
                    count+=1
        return count