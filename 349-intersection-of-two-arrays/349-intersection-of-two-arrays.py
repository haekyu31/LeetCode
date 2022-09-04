class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1= sorted(list(set(nums1)))
        
        output = []
        for i in range(len(nums1)):
            j = 0
            while j < len(nums2):
                if nums1[i] == nums2[j]:
                    output.append(nums1[i])
                    break
                else : 
                    j += 1
        return output
                    
                