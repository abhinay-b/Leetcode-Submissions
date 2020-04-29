class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m,n = len(matrix),len(matrix[0])
        memo = [[0]*n for _ in range(m)]
        for j in range(0,n):
            memo[0][j] = (int)(matrix[0][j])
        for i in range(0,m):
            memo[i][0] = (int)(matrix[i][0])
        maxVal = max(memo[0])
        for i in range(1,m):
            maxVal = max(maxVal,memo[i][0])
            for j in range(1,n):
                if matrix[i][j] == '1':
                    memo[i][j] = 1
                    for x,y in [[i-1,j],[i-1,j-1],[i,j-1]]:
                        if 0 <= x < m and 0 <= y < n:
                            memo[i][j] = min(memo[i][j],memo[x][y])
                    memo[i][j] += 1
                    maxVal = max(maxVal, memo[i][j])
        return maxVal**2
