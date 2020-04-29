class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp = 0
        for i in range(len(nums)):
            temp ^= nums[i]
        return temp
