class Solution:
    def DFS(self, grid, idx_x, idx_y):
        if idx_x <0 or idx_y <0 or idx_x >=self.x or idx_y >= self.y or grid[idx_y][idx_x] == 0 :
            return 
        grid[idx_y][idx_x] = 0
        self.Count += 1 
        self.DFS(grid, idx_x, idx_y+1)
        self.DFS(grid, idx_x+1, idx_y)
        self.DFS(grid, idx_x, idx_y-1)
        self.DFS(grid, idx_x-1, idx_y)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.island = []
        self.Count = 0
        self.y, self.x = len(grid), len(grid[0])
        for idx_y in range(self.y):
            for idx_x in range(self.x):
                if grid[idx_y][idx_x] == 1:
                    self.DFS(grid,idx_x, idx_y)
                    self.island.append(self.Count)
                    self.Count = 0
        if not self.island:
            return 0
        return max(self.island)
