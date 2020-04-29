class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[False]*n for _ in range(n)]
        dp[0][0] = dp[n-1][n-1] = True
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if nums[i] > 0:
                    dp[i][j] = True
                    nums[i] -= 1
                dp[i][n-1] = dp[i][j] and dp[j][n-1]
#                 print(dp[i][n-1],i,j)
                if dp[i][n-1]:
                    break
        return dp[0][n-1]
