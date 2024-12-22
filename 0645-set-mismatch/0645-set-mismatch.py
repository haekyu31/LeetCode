class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_counts = [0] * (len(nums) + 1)
        for num in nums:
            num_counts[num] += 1
            
        print(num_counts)
        
        duplicate = -1
        missing = -1
        
        for i in range(1, len(nums) + 1):
            if num_counts[i] == 2:
                duplicate = i
            elif num_counts[i] == 0:
                missing = i
                
        return [duplicate, missing]