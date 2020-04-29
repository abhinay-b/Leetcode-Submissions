class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if max(nums) < 0:
            return max(nums)
        sumSub = start = end = maxSum = 0
        for idx,num in enumerate(nums):
            sumSub += num
            if sumSub < 0:
                start = idx+1
                sumSub = 0
            elif maxSum < sumSub:
                end = idx
                maxSum = sumSub
        return maxSum
