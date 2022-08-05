class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
#             HashTable
#             HashTable = {}
#             for i, value in enumerate(nums):
#                 HashTable[value] = i
#             Triplets = [-i for i in nums]
#             Pairs = [i for i in Triplets]
            
            #two pointer
            Answer = set()
            nums.sort()
            for i in range(len(nums)-2):
                j,k= i+1, len(nums)-1
                while j < k:
                    if nums[i]+nums[j]+nums[k] >0:
                        k -= 1
                    elif nums[i]+nums[j]+nums[k]<0:
                        j += 1
                    else :
                        Answer.add(tuple([nums[i],nums[j],nums[k]]))
                        j,k = j+1, k-1
            
            return list(Answer)
                