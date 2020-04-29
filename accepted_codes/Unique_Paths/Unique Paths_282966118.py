class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 1
        path = [[0]*n for _ in range(m)]
        for j in range(n):
            path[0][j] = 1
        for i in range(m):
            path[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                path[i][j] += path[i-1][j] + path[i][j-1]
        return path[m-1][n-1]
