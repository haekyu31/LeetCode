class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res = 0
        rows = len(mat)
        cols = len(mat[0])
        
        rowtotals = []
        coltotals = []
        
        # Store the sum of each row
        for row in mat:
            rowtotals.append(sum(row))
        
        # Store the sum of each column
        for col in zip(*mat):
            coltotals.append(sum(col))
        
        # Check if current position is "1" and is the only "1" in that row and column
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and rowtotals[i] == 1 and coltotals[j] == 1:
                    res += 1
        
        
        return res