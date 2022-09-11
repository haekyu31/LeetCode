class Solution:
    def convertToTitle(self, n: int) -> str:
        Answer = ""
        while n>0:
            Answer  =  chr(ord("A") + (n - 1) % 26) + Answer  # 0부터 가야하니까 n-1로 줄여주고 아스키 코드를 사용하기 위해서 ord("A")를 더한다
            n = (n-1)//26                           
        return Answer