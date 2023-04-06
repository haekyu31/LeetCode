class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)
#         freqs = collections.Counter(stones)
#         count = 0
        
#         for char in jewels:
#             count += freqs[char]
#         return count
# #         freqs = {}
#         count = 0
        
#         # 돌의 빈도 수 계산
#         for char in stones :
#             if char not in freqs:
#                 freqs[char] = 1
#             else:
#                 freqs[char] += 1
                
#         # 보석의 빈도 수 합산
#         for char in jewels:
#             if char in freqs:
#                 count += freqs[char]
#         return count