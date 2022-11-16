class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k+1, len(numbers)-1
            expected = target -v
            # 이진 검색으로 나머지 값 판별
            
            while left <= right:
                mid = (left+right)//2
                if numbers[mid] < expected:
                    left = mid+1
                elif numbers[mid] > expected:
                    right = mid-1
                else:
                    return k+1, mid +1
#         left, right = 0, len(numbers)-1
#         while not left == right:
#             if numbers[left] + numbers[right] < target:
#                 left +=1
#             elif numbers[left] + numbers[right] > target:
#                 right -=1
#             else:
#                 return left+1, right+1
                