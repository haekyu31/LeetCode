class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
#         K = 10000
#         element_to_count = [0]*(2*K+1)
#         for element in nums:
#             element_to_count[element+K] +=1
            
#         max_sum = 0
#         is_even_index = True
#         for element in range(2*K+1):
#             while element_to_count[element] >0:
#                 if is_even_index:
#                     max_sum += element -K
#                 is_even_index = not is_even_index;
#                 element_to_count[element] -=1
#         return max_sum
        nums.sort()
        max_sum = 0
        for i in range(0, len(nums),2):
            max_sum += nums[i]
        return max_sum