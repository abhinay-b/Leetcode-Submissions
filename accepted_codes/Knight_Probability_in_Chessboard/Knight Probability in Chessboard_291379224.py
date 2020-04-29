from functools import reduce
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1
        if N < 3:
            return 0
        res = 0
        prev = [[0]*N for _ in range(N)]
        prev[r][c] = 1
        for _ in range(K):
            curr = [[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for m,n in [(i+1,j+2),(i+1,j-2),(i-1,j+2),(i-1,j-2),(i+2,j+1),(i+2,j-1),(i
                        -2,j+1),(i-2,j-1)]:
                        if 0 <= m < N and 0 <= n < N:
                            curr[m][n] += prev[i][j] / 8
            prev = curr
        return sum(map(sum,curr))
