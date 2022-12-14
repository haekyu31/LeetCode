class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i in range(len(mat)):
            for j in range(i, len(mat)):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            mat[i].reverse()
