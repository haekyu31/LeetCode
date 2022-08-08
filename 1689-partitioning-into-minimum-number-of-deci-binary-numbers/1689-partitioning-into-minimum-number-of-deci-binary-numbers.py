class Solution:
    def minPartitions(self, n: str) -> int:
        # str을 숫자로 바꾸고 리스트로 자리수에 맞게 나눠준다
        list_n = [int(i) for i in list(n)]
        print(list_n)
        
        # 각 자리수별 숫자가 0이 아니라면 1을 빼주고 아니라면 0이라고 둔다
        Answer = []
        current_li = []
        while max(list_n)>0:
            for i in range(len(list_n)):
                if list_n[i] > 0:
                    current_li.append(1)
                    list_n[i] -=1
                else: 
                    current_li.append(0)
                    list_n[i] = 0
            Answer.append(current_li)
        return len(Answer)
            