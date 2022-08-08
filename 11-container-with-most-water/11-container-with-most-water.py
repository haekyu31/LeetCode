class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        Answer =0
        i = 0
        j = len(height)-1    
        while i < j:
            water = (j-i)* min(height[i], height[j])
          
            if Answer < water:
                Answer = water
            if height[i] >height[j]:
                j -=1
            else:
                i +=1
        return Answer