class Solution:
    def romanToInt(self, s: str) -> int:
        list_s  = list(s)
        Answer, Prev = 0, 0
        Roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        num = [1,5,10,50,100,500,1000]
        roman = dict(zip(Roman, num))
        li = list_s[::-1]
        for i in li:
            if roman[i] >=Prev:
                Answer += roman[i]
            else :
                Answer -= roman[i]
            Prev = roman[i]
        return Answer
    
    
    # dict로 Roman과 int를 정렬한다
    # 숫자를 뒤에서 부터 세야 하기때문에 뒤집고 
    # roman의 숫자가 이전의 숫자보다 큰경우 숫자를 빼주고 이전의 숫자보다 큰경우는 더해준다
    # 계산하고 한칸씩 포인터를 옮겨준다