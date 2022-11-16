class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result:Set = set()
        # 양쪽 모두 정렬
        nums1.sort()
        nums2.sort()
        i = j = 0
        # 투 포인터 우측으로 이동하며 일치 여부 판별
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i+=1
                j+=1
        return result
    
        # result:Set = set()
        # nums2.sort()
        # for n1 in nums1:
        #     # 이진 검색으로 일치 여부 판별
        #     i2 = bisect.bisect_left(nums2, n1)
        #     if len(nums2)> 0 and len(nums2) > i2 and n1 == nums2[i2]:
        #         result.add(n1)
        # return result