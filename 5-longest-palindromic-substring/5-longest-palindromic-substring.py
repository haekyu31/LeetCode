class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 홀수인 경우 index로 접근 
        # 좌우 인덱스를 확인해서 palindromic이면 늘어난 걸로 바뀐다
        # 좌우 인덱스를 추가한게 같지 않다면 끝난다
        # 다음 str를 확인 
        
        # 짝수인 경우 index로 접근
        # 좌우 인덱스 확인
        # 좌우 인덱스를 확인해서 palindromic이면 늘어난 걸로 바뀐다
        # 좌우 인덱스를 추가한게 같지 않다면 끝난다
        # 다음 두개의 str를 확인 
              
        if len(s) <= 1:
            return s
        i,l=0,0
        for j in range(len(s)):
            if s[j-l: j+1] == s[j-l: j+1][::-1]:
                i, l = j-l, l+1
                # print(s[i: i+l])
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i, l = j-l-1, l+2
                # print(s[i: i+l])
        return s[i: i+l]
    
        # # 가장 긴 palindrome인지 체크하기 위한 len 변수
        # MaxLen = 0
        # MaxPal = ""
        # # 홀수 palindrome에 대한 for loop
        # for i in range(len(s)):
        #     j = 0 #i는 palindrome의 가장 중심, j는 i에서 몇개만큼 옆으로 확장할것인가
        #     while s[i-j] == s[i+j]:
        #         if MaxLen < len(s[i-j:i+j+1]): #현재 palindrome이 maxlen보다 큰지 확인
        #             MaxLen = len(s[i-j:i+j+1])
        #             MaxPal = s[i-j:i+j+1]
        #         j += 1
        #         if i-j < 0 or i+j >= len(s):
        #             break
        # # 짝수 palindrome에 대한 for loop
        # for i in range(len(s)-1):
        #     j = 0
        #     while s[i-j] == s[i+j+1]:
        #         if MaxLen < len(s[i-j:i+j+2]):
        #             MaxLen = len(s[i-j:i+j+2])
        #             MaxPal = s[i-j:i+j+2]
        #         j += 1
        #         if i-j < 0 or i+j+1 >= len(s):
        #             break
        # return MaxPal