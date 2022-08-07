class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        Answer = []
        
        for i in range(numRows):
            row = [0 for _ in range(i+1)]
            row[0] = 1
            row[-1] = 1
            
            for j in range(1, len(row)-1):
                row[j] = Answer[i-1][j-1] + Answer[i-1][j]
                
            Answer.append(row)
        return Answer