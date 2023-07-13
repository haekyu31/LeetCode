class Solution:
    def binaryGap(self, n: int) -> int:
        if(bin(n).count('1'))==1:
            return 0
        c=0
        x=bin(n)[2:]
        for i in range(len(x)):
            if(x[i]=='1'):
                j=i+1
                while j<len(x):
                    if(x[j]=='1'):
                        c=max(j-i,c)
                        break
                    j+=1
        return c