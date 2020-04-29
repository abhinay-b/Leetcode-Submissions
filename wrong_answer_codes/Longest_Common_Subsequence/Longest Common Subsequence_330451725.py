class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        if m > n:
            m,n = n,m
            text1,text2 = text2,text1
        memo = [[0]*n for _ in range(m)]
        dx = [0,-1]
        dy = [-1,0]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    memo[i][j] = memo[i-1][j] + 1
                    # print(i,j,memo[i][j],memo[i-1][j-1])
                else:
                    for k in range(2):
                        if 0 <= i+dx[k] < m and 0 <= j+dy[k] < n:
                            memo[i][j] = max(memo[i][j], memo[i+dx[k]][j+dy[k]])
        return memo[-1][-1]
                        
