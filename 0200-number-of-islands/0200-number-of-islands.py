class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            # 더이상 땅이 아닌경우 종료
            if i <0 or i>=len(grid) or \
                j<0 or j>=len(grid[0]) or \
                grid[i][j] != '1':
                    return
            # 방문처리 
            grid[i][j] = 0      
            
            # 동서남북 탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        # 섬의 갯수 count
        count =0
        
        # 2차원 그래프 접근 방식
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =='1':
                    dfs(i,j)
                    # 모든 육지 탐색후 count 1 증가
                    count +=1
        return count