class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hashset = {}

        for i in range(len(items1)):
            if items1[i][0] in hashset:
                hashset[items1[i][0]] += items1[i][1]
            else:
                hashset[items1[i][0]] = items1[i][1]

        for i in range(len(items2)):
            if items2[i][0] in hashset:
                hashset[items2[i][0]] += items2[i][1]
            else:
                hashset[items2[i][0]] = items2[i][1]
        
        ans = []

        for i in sorted(hashset):
            ans.append([i, hashset[i]])
        
        return ans