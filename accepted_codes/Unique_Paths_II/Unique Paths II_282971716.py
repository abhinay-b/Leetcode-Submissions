class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        n,m = len(obstacleGrid[0]),len(obstacleGrid)
        if n == 1 or m == 1:
            if 1 in obstacleGrid[0] or [1] in obstacleGrid:
                return 0
            else:
                return 1
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        path = [[0]*n for _ in range(m)]
        path[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    path[i][j] = 0
                else:
                    if i > 0:
                        path[i][j] += path[i-1][j]
                    if j > 0:
                        path[i][j] += path[i][j-1]
                # print(path)
        return path[m-1][n-1]
