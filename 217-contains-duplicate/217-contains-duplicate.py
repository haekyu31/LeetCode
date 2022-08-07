class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)
        for i in c.items():
            if i[1] == 1:
                continue
            else: return True
        