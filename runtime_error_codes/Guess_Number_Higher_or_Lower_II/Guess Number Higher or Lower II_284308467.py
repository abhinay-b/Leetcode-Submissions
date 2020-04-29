class Solution:
    def getMoneyAmount(self, n: int) -> int:
        guess = [[0]*(n+1) for _ in range(n+1)]
        start = 1
        for end in range(2,n+1):
            i,j = start,end
            while i < n and j < n+1:
                res = float('inf')
                for k in range(i,j):
                    temp = k + max(guess[i][k-1], guess[k+1],j)
                    res = min(temp,res)
                guess[i][j] = res
                i += 1
                j += 1
        return guess[1][n]
        
