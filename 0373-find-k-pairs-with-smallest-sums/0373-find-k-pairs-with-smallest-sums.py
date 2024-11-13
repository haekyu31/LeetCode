import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # nums1, nums2에서 합이 가장 작은 k개의 쌍을 구한다.
        # heap을 활용하여 (sum, num1, num2, i, j) heap에 k개의 쌍이 채워질 때 까지 반복하도록
        heap = [(nums1[0] + nums2[0], nums1[0], nums2[0], 0, 0)]
        visited = set((0,0))
        result = []
        
        while heap and len(result) < k:
            _, num1, num2, i, j = heapq.heappop(heap)
            result.append([num1, num2])
            
            if i < len(nums1) - 1 and (i+1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], nums1[i+1], nums2[j], i+1, j))
                visited.add((i+1, j))
                
            if j < len(nums2) - 1 and (i, j+1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], nums1[i], nums2[j+1], i, j+1))
                visited.add((i, j+1))
                
        return result
