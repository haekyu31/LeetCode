class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 카데인 알고리즘 
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum
    
        # 앞에서부터 계속 값을 계산하면서 누적합을 계산
        # 이전값이 0 보다 작은경우는 최댓값과 관계 없으므로 버린다.
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i-1] if nums[i-1] >0 else 0
        # return max(nums)
    
        
        