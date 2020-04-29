class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[False]*n for _ in range(n)]
        dp[0][0] = True
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if nums[i] > 0:
                    dp[i][j] = True
                    nums[i] -= 1
                else:
                    for k in range(i+1,j):
                        dp[i][j] = dp[i][k] and dp[k][j]
                        if dp[i][j]:
                            break
        return dp[0][n-1]
