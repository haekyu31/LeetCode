class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 3가지 숫자가 크기순으로 있는지 확인하기
        # i,j를 기준으로 잡고 k찾기
        i = j = float('inf')
        
        for num in nums:
            if num <= i: 
                i = num # triplet에서 가장 작은수 i
            elif num <= j:  # triplet에서 i 보다 큰 수가 나온다면
                j = num
            else:           # j 보다 큰 수가 나온다면 triplet
                return True
        return False