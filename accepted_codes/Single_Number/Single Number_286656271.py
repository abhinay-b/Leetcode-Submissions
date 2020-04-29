class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp = nums[0]
        for num in nums[1:]:
            temp ^= num
        return temp
