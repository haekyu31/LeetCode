class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # 1개 단어만 있는 경우
        if len(words) < 2:
            res = []
            for char in words[0]:
                res.append(char)
            return res
                
        res = []
        word1 = set(words[0])
        for char in word1:
            # 첫번째 단어에서 중복을 set로 제거한 후 count를 사용하여 최대 중복 횟수를 frequency에 저장한다.
            frequency = min([word.count(char) for word in words])
            # 최대 중복 횟수만큼 res에 저장한다.
            res += [char] * frequency
        return res