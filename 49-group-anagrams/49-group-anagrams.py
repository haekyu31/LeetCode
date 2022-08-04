class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            # 1st step list요소를 list로 바꾼다 ["eat"] -> ["e","a","t"]
            # 2nd step Counter()를 통해서 각 list의 문자 갯수를 확인한다.
            # 3rd step 반복문을 통해서 Counter()가 동일한 list 끼리 더해준다
            # 4th step 더한 list를 list로 묶어준다
            # 처음 내가 생각한 방법
            
            #인덱스를 통해서 구하는 방법
            Sorted = [''.join(sorted(str)) for str in strs]  # 문자열로 바꾼후 리스트로 넣고 sorted로 반환하고 하나의 문자로 join한다
            Sorted_unique = list(set(Sorted))                # join한 문자중 중복된것이 있는지 set로 확인하고 list로 바꿔준다
            # print(strs)                                    ["eat","tea","tan","ate","nat","bat"]
            # print(Sorted)                                  ["aet","aet","ant","aet","ant","abt"]               
            # print(Sorted_unique)                           ["abt","ant","aet"]   
            
            Answer = []
            for i in range(len(Sorted_unique)):              # index로 접근
                Answer.append([])                            # unique한 갯수만큼 빈 list를 만들어준다
            for i in range(len(Sorted)):                     # index로 접근
                Answer[Sorted_unique.index(Sorted[i])].append(strs[i])
                
            return Answer
                    
                