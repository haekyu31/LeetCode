class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        res = []
        for i, v in enumerate(nums):
            while q and nums[q[-1]] <= v:
                q.pop()
            q.append(i)
            
            if q[0] == i-k:
                q.popleft()
            if i >= k-1:
                res.append(nums[q[0]])
        return res