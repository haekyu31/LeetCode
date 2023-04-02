class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = [''.join(sorted(str)) for str in strs]
        # print(sorted_list)
        sorted_unique = list(set(sorted_list))
        # print(sorted_unique)
        
        answer = []
        for i in range(len(sorted_unique)):
            answer.append([])
        # print(answer)
        for i in range(len(sorted_list)):
            answer[sorted_unique.index(sorted_list[i])].append(strs[i])
        # print(answer)
        return answer