# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums1= sorted(list(set(nums1)))
        
#         output = []
#         for i in range(len(nums1)):
#             j = 0
#             while j < len(nums2):
#                 if nums1[i] == nums2[j]:
#                     output.append(nums1[i])
#                     break
#                 else : 
#                     j += 1
#         return output
# class Solution:
#     def set_intersection(self, set1, set2):
#         return [x for x in set1 if x in set2]
        
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """  
#         set1 = set(nums1)
#         set2 = set(nums2)
        
#         if len(set1) < len(set2):
#             return self.set_intersection(set1, set2)
#         else:
#             return self.set_intersection(set2, set1)
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)                