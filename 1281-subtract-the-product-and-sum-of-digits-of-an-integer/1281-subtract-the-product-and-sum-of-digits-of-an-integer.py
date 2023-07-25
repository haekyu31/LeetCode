class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numbers = list(str(n))
        num_pro = 1
        num_sum = 0
        for num in numbers:
            num_pro *= int(num)
        for num in numbers:
            num_sum += int(num)
        
        return num_pro - num_sum