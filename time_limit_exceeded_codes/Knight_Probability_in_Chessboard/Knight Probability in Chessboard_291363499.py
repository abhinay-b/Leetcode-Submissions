from collections import deque
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1
        if N < 3:
            return 0
        queue = deque([(r,c,1,0)])
        res = 0
        while queue:
            i,j,prob,k = queue.pop()
            if k == K:
                res += prob
            else:
                for m,n in [(i-1,j-2),(i-1,j+2),(i+1,j-2),(i+1,j+2),(i+2,j-1),(i+2,j+1),(i-2,j
                    -1),(i-2,j+1)]:
                    if 0 <= m < N and 0 <= n < N:
                        queue.appendleft((m,n,prob*0.125,k+1))
        return res
