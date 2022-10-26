class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ', paragraph)  # ^은 not을 의미 \w는 단어문자 re.sub()는 단어문자가 아닌것을 모두 공백으로 바꾼다, paragraph에서
                .lower().split()
                if word not in banned]
        counts = collections.Counter(words)  # Counter 를 이용해서 word가 몇번 등장했는지
        return counts.most_common(1)[0][0]  # counts 에서 가장 많이 등장한 most_common의 첫번째 값을 counts.most_common(1)로 가져온다