class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        wealth = nums.copy()
        for i in range(2,len(nums)):
            wealth[i] += wealth[i-2]
        return max(wealth)
