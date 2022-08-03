class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        digits = ''.join(digits)
        digits = int(digits) + 1
        answer = list(str(digits))
        
        return answer