class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        words_index = defaultdict(int)
        for i, w in enumerate(words):
            words_index[w] = i
        
        dp = [1] * len(words) + [0]
        res = 1
        for i in range(len(words) - 1, -1, - 1):
            for j in range(len(words[i])):
                new_word = words[i][:j] + words[i][j+1:]
                if new_word in words_index:
                    dp[i] = max(dp[i], 1 + dp[words_index[new_word]])
            res = max(res, dp[i])
        return res
