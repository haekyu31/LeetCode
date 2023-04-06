class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}
        count = 0
        
        # 돌의 빈도 수 계산
        for char in stones :
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
                
        # 보석의 빈도 수 합산
        for char in jewels:
            if char in freqs:
                count += freqs[char]
        return count