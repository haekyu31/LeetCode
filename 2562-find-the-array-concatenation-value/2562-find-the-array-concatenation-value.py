class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n=len(nums)

        ans=nums[n//2] if n%2 else 0

        for i in range(n//2): 
            ans += int(str(nums[i])+str(nums[-i-1]))
        
        return ans