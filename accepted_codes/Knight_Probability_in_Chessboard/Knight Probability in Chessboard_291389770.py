from collections import defaultdict
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1
        if N < 3:
            return 0
        res = 0
        prev = [[0]*N for _ in range(N)]
        prev[r][c] = 1
        dictn = defaultdict(list)
        for _ in range(K):
            curr = [[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    if (i,j) not in dictn:
                        for m,n in [(i+1,j+2),(i+1,j-2),(i-1,j+2),(i-1,j-2),(i+2,j+1),(i+2,j-1
                            ),(i-2,j+1),(i-2,j-1)]:
                            if 0 <= m < N and 0 <= n < N:
                                dictn[(i,j)].append((m,n))
                    for m,n in dictn[(i,j)]:
                        curr[i][j] += prev[m][n] / 8
            prev = curr
        return sum(map(sum,curr))
