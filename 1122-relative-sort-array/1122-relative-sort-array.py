class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for x in arr2:
            while x in arr1:
                res.append(x)
                arr1.remove(x)
            # print(arr1)
        return res+ sorted(arr1)