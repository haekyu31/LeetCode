class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort() # two pointer 는 정렬된 상태에서 사용해야 한다
        
        for i in range(len(nums) -2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left, right = i+1, len(nums)-1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0 :
                    left += 1
                elif sum >0 :
                    right -= 1
                else:
                    # sum = 0 정답 및 스킵 처리
                    results.append([nums[i] , nums[left], nums[right]]) # results에 정답을 저장
                    
                    while left < right and nums[left] == nums[left+1]:  # 중복일 때 건너 뛰기
                        left += 1
                    while left < right and nums[right] == nums[right -1]:   # 중복일 때 건너 뛰기
                        right -= 1
                    left += 1   # point움직이기
                    right -= 1  # point움직이기
        return results