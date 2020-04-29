class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def growIsland(i,j):
            for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= a < m and 0 <= b < n and grid[a][b] == '1':
                    grid[a][b] = "-1"
                    growIsland(a,b)
        if not grid or not grid[0]:
            return 0
        m,n = len(grid),len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    growIsland(i,j)
        return count
