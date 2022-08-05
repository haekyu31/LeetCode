class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Double for loop
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return[i,j]
        
        # n squared 알고리즘
        # pair = [target -i for i in nums]   
        # for i, n in enumerate(pair):
        #   if n in nums and i != nums.index(n):
        #       return [i, nums.index(n)]
        
        # HashTable 알고리즘
      #  HashTable = {}
      #  for i, value in enumerate(nums):
      #      HashTable[value] = i
      #  Pairs = [target -i for i in nums] 
      #  
      #  for i, Pair in enumerate(Pairs):
      #      if Pair in HashTable and i != HashTable[Pair]:
      #          return [i, HashTable[Pair]]
            
        # two pointer  정렬이 되어있다면
        num_sorted = sorted(nums)
        i = 0
        j = len(num_sorted)-1
        while i < j :
            left = num_sorted[i] 
            right = num_sorted[j]
            sum = left + right
            
            if sum > target:
                j -= 1
            elif sum < target:
                i +=1
            else :
                break
        if num_sorted[i] != num_sorted[j] :
            return nums.index(left), nums.index(right)
        else:
            return [i for i, num in enumerate(nums) if num == left]
        
# n = 5 # 데이터의 개수 N
# m = 5 # 찾고자하는 부분합 M
 
# count = 0
# interval_sum = 0
# end = 0
 
# # start를 차례대로 증가시키며 반복
# for start in range(n):
#     # end만큼 이동시키기
#     while interval_sum < m and end < n:
#         interval_sum += data[end]
#         end += 1
#     # 부분합이 m일 때 카운트 증가
#     if interval_sum == m:
#         count += 1
#     interval_sum -= data[start]
 
# print(count)
        
        
        