class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = collections.Counter(arr)
        print(c.items())
        Answer = [-1]
        for i, n in c.items():
            if i == n:
                Answer.append(i)
        return max(Answer)
        #    if i == i.value:
        #        return i
        #    else: return -1
            