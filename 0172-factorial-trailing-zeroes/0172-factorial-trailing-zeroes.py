class Solution:
    def trailingZeroes(self, n: int) -> int:
        quotient = n // 5
        return quotient + self.trailingZeroes(quotient) if quotient >= 5 else quotient