class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True

        total = sum(nums)

        if total & 1:
            return False

        total //= 2

        dp = [[sum_ == 0 for sum_ in range(total + 1)] for _ in range(len(nums) + 1)]
        for i, num in enumerate(nums, start=1):
            for sum_ in range(total + 1):
                dp[i][sum_] = dp[i - 1][sum_] or sum_ >= num and dp[i - 1][sum_ - num]

        return dp[-1][-1]
