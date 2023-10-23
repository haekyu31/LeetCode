class Solution:
    def vowelStrings(self, ws: List[str], l: int, r: int) -> int:
        return sum({w[0], w[-1]} < {'a', 'e', 'i', 'o', 'u'} for w in ws[l:r+1])      