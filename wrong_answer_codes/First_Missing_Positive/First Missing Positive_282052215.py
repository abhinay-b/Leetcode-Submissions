class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        for idx,num in enumerate(nums):
            if num <= 0:
                nums[idx] = len(nums)+1
        for num in nums:
                idx = abs(num) - 1
                if idx < len(nums) and nums[idx] > 0:
                    nums[idx] *= -1
        for idx,num in enumerate(nums,1):
                if num > 0:
                    return idx
