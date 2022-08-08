class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:       
        # nums 정렬한다
        # i 를 기준으로 잡고 j k 를 two point 로 돌린다
        # nums_sum을 리스트에 넣는다. 
        # target과의 차이를 또다른 리스트에 넣고 절대값이 가장 작은수의 인덱스를 구한다
        # nums_sum에서 인덱스에 위치한 값을 가져온다.
        # nums 가 3개로만 이루어졌을경우
        # target이 0인경우
        
        
        AnswerSum = 999999
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                CurrentSum = nums[i] + nums[j] +nums[k]
                if abs(CurrentSum- target)<abs(AnswerSum-target):
                    AnswerSum = CurrentSum
                
                if CurrentSum > target:
                    k -= 1
                elif CurrentSum < target:
                    j += 1
                else :
                    return CurrentSum
        return AnswerSum 