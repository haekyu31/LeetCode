class Solution:
    def DFS(self, number, sequence):
        if not number:   # 더이상 돌 수 있는 단어가 없을때
            
            self.Answer.append("".join(sequence))
        if number:
            Char = number.pop(0) #첫번째 숫자를 꺼낸다
            for i in self.dic1[Char]: #첫번째 숫자의 딕셔너리 단어만큼 반복하면서 
                print(number, Char, sequence, self.Answer) # sequence는 계속 할당 되어야하기 때문에 copy를 하지 않는다.
                self.DFS(number[:], sequence+[i]) # sequence에 단어를 더한상태로 다음 DFS를 돌기 변화는 얕은 복사를 한상태로
    def letterCombinations(self, digits: str) -> List[str]:
        self.dic1 = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        Digits = list(digits)
        self.Answer = []
        self.DFS(Digits[:],[])  #얕은복사 새로운 주소를 갖지만 reference는 같은 값을 갖도록 한다   
        
        return self.Answer
        
        