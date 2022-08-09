class Solution:
    def minPartitions(self, n: str) -> int:
        Answer = []
        list_n = [int(i) for i in list(n)]
        while max(list_n)>0:             # 가장 큰 수만큼 반복하도록 
            current = []                 # 한번 for loop을 돈다음 current를 초기화 해주는 작업   
            for i in range(len(list_n)): # 자릿수에 숫자가 0이 아니라면 1을 current에 더해주는 방식
                if list_n[i] > 0:
                    current.append(1)
                    list_n[i] -=1
                else:
                    current.append(0)   
            Answer.append(current)       # for loop 한바퀴를 돌았을때 Answer 리스트에 넣기
        return (len(Answer))
    
    
    
#     # 1689 기본풀이
# class Solution:
#     def minPartitions(self, n: str) -> int:
#         nList = [int(i) for i in list(str(n))]
#         return max(nList)
# # 1689 Greedy 알고리즘 출력 풀이
# class Solution:
#     def minPartitions(self, n: str) -> int:
#         InputList = [ int(i) for i in list(n) ]
#         MinusList = []
#         nCount = 0
#         while sum(InputList) != 0:
#             Minus = []
#             for i, digit in enumerate(InputList):
#                 if digit != 0:
#                     Minus.append(1)
#                     InputList[i] -= 1
#                 elif digit == 0:
#                     Minus.append(0)
#             Minus = ''.join([str(i) for i in Minus])
#             MinusList.append(Minus)
#             nCount += 1
#         print(MinusList)
#         return nCount
#         # return max([ int(i) for i in list(n)])