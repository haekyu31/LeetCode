class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        rn = ransomNote
        mz = magazine
        
        rn_li = list(rn)
        mz_li = list(mz)
        
        
        Answer = True
        
        for i in rn_li:
            if i not in mz_li:
                Answer = False
                break
            else:
                mz_li.pop(mz_li.index(i)) #한줄로 만들기
            
            
        return Answer
    
    #google에 영작해서 구글링하기