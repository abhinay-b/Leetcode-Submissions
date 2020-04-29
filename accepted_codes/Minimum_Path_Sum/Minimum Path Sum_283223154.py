class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        m,n = len(grid),len(grid[0])
        temp = grid.copy()
        for row in range(1,m):
            temp[row][0] += temp[row-1][0]
        for col in range(1,n):
            temp[0][col] += temp[0][col-1]
        for row in range(1,m):
            for col in range(1,n):
                    temp[row][col] += min(temp[row-1][col],temp[row][col-1])
        return temp[m-1][n-1]
                    
