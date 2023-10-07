class Solution:
    def sortString(self, s: str) -> str:
        res = ''
        counter = dict(collections.Counter(s))
        chars = sorted(list(set(s)))
        
        while(counter):
            for char in chars:
                if char in counter:
                    res += char
                    counter[char] -= 1
                    if counter[char] == 0:
                        del counter[char]
            for char in reversed(chars):
                if char in counter:
                    res += char
                    counter[char] -= 1
                    if counter[char] == 0:
                        del counter[char]
                        
        return res