class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def minCost(m,n):
            if m < 0 or n < 0:
                return float('inf')
            if m == 0 and n == 0:
                return grid[m][n]
            return min(minCost(m-1,n), minCost(m,n-1)) + grid[m][n]
        if not grid:
            return -1
        m = len(grid)
        n = len(grid[0])
        return minCost(m-1,n-1)
