class Solution:
    
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:    
        paragraph = paragraph.replace(',', ' ')
        paragraph = paragraph.replace('  ', ' ')
        words = paragraph.lower().split()
        word_list = []
        for s in words :
            s = ''.join(e for e in s if e.isalnum())
            word_list.append(s)
        
         #ban에 포함되어있는 단어들 모두 pop 하여 삭제
        for ban in banned:
            while ban in word_list:
                word_list.pop(word_list.index(ban))
        # 가장 많이 count 된 문자열 return
        return max(word_list,key=word_list.count)
        