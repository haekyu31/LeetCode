class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_list = list(jewels)
        stone_list = list(stones)
        count = 0
        for i in stone_list:
            if i in jewels_list:
                count +=1
        return count