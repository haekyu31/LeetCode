class Solution:
    def reverseVowels(self, s: str) -> str:
        it = (ch for ch in s[::-1] if ch.lower() in 'aeiou')
        return ''.join(next(it) if ch.lower() in 'aeiou' else ch for ch in s)