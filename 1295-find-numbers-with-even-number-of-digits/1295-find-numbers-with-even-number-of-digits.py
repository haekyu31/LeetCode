class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        answer = 0
        for i in nums:
            n = 0
            while i // 10**(n) != 0 : 
                n += 1
            else : 
                if n % 2 == 0:
                    answer += 1
        return answer

        