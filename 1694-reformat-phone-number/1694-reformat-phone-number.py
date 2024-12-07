class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-", "").replace(" ", "") # removing - and space 
        ans = []
        for i in range(0, len(number), 3): 
            if len(number) - i != 4: ans.append(number[i:i+3])
            else: 
                ans.extend([number[i:i+2], number[i+2:]])
                break 
        return "-".join(ans)