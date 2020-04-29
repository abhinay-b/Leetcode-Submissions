class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        if len(obstacleGrid) == 1 or len(obstacleGrid[0]) == 1:
            if 1 in obstacleGrid[0] or [1] in obstacleGrid:
                return 0
            else:
                return 1
        
        n,m = len(obstacleGrid[0]),len(obstacleGrid)
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        path = [[0]*n for _ in range(m)]
        for j in range(n):
            path[0][j] = 1
        for i in range(m):
            path[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i-1][j] == 0:
                    path[i][j] += path[i-1][j]
                if obstacleGrid[i][j-1] == 0:
                    path[i][j] += path[i][j-1]
        return path[m-1][n-1]
