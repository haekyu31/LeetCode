class Solution:
    def readBinaryWatch(self, n: int) -> List[str]:
        return [str(h)+':'+'0'*(m<10)+str(m) for h in range(12) for m in range(60) if (bin(m)+bin(h)).count('1') == n]