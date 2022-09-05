class Solution:
    def DFS(self, number, sequence):
        if not number:   # 더이상 돌 수 있는 단어가 없을때
            self.Answer.append("".join(sequence))
        if number:
            Char = number.pop(0) #첫번째 숫자를 꺼낸다
            for i in self.dic1[Char]: #첫번째 숫자의 딕셔너리 단어만큼 반복하면서 
                self.DFS(number[:], sequence+[i]) # sequence에 단어를 더한상태로 다음 DFS를 돌기
    def letterCombinations(self, digits: str) -> List[str]:
        self.dic1 = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        Digits = list(digits)
        self.Answer = []
        self.DFS(Digits,[])
        
        return self.Answer
        
        