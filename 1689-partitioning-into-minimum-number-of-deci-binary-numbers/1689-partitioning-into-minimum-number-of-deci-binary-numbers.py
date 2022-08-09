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