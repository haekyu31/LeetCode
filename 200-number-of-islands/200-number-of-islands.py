class Solution:
    def DFS(self, grid, idx_x, idx_y):
        if idx_x <0 or idx_y <0 or idx_x >=self.x or idx_y >= self.y or grid[idx_y][idx_x] == "0" :
            return 
        grid[idx_y][idx_x] = "0"
        self.DFS(grid, idx_x, idx_y+1)
        self.DFS(grid, idx_x+1, idx_y)
        self.DFS(grid, idx_x, idx_y-1)
        self.DFS(grid, idx_x-1, idx_y)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        self.Count = 0
        self.y, self.x = len(grid), len(grid[0])
        for idx_x in range(self.x):
            for idx_y in range(self.y):
                if grid[idx_y][idx_x] == "1":
                    self.Count +=1
                    self.DFS(grid,idx_x, idx_y)
        return self.Count