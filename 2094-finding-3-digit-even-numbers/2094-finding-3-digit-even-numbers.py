class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # 첫번째로 올 수 있는 경우의 수: 0 뺴고 전부다...
        # 두번째는 모두가 올 수 있음..
        # 세번째: 짝수만 올 수 있음..
        # 위 조건을 만족하는 3가지 index (First, Second, Third)를 for loop를 돌면서
        # 같은 숫자를 동시에 쓰는지에 대한 if 조건만 주시면
        # 모든 숫자를 만들어 낼 수 있다!
        # 그리고 정렬하면 정답
        
        
        First = [i for i, digit in enumerate(digits) if digit != 0]
        Second = list(range(0, len(digits)))
        Last = [i for i, digit in enumerate(digits) if digit %2 == 0]
        Answer = set()
        for i in First:
            for j in Second:
                for k in Last:
                        if i != j and i != k and j != k:
                            Answer.add(digits[i]*100 + digits[j]*10 + digits[k])
        Answer = list(Answer)
        Answer.sort()
        return Answer
