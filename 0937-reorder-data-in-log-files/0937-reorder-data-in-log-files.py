class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key = self.sort)
    def sort(self, logs):
        a, b = logs.split(' ', 1)
        if b[0].isalpha():
            # print(0, b, a)
            return (0,b,a)
        else:
            return (1,None,None)