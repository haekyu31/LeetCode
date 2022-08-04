class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # jewels_list = list(jewels)
        # stone_list = list(stones)
        # count = 0
        # for i in stone_list:
        #     if i in jewels_list:
        #         count +=1
        # return count
    
    
        stone_count = collections.Counter(stones)
        jwel_list = list(jewels)
        answer = 0
        for i in stone_count.items():
            if i[0] in jwel_list:
                answer += i[1]
        return answer   