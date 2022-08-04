class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            # 1st step list요소를 list로 바꾼다 ["eat"] -> ["e","a","t"]
            # 2nd step Counter()를 통해서 각 list의 문자 갯수를 확인한다.
            # 3rd step 반복문을 통해서 Counter()가 동일한 list 끼리 더해준다
            # 4th step 더한 list를 list로 묶어준다
            
            
            Sorted = [''.join(sorted(str)) for str in strs]
            Sorted_unique = list(set(Sorted))
            # print(strs)
            # print(Sorted)
            # print(Sorted_unique)
            
            Answer = []
            for i in range(len(Sorted_unique)):
                Answer.append([])
            for i in range(len(Sorted)):
                Answer[Sorted_unique.index(Sorted[i])].append(strs[i])
                
            return Answer
                    
                