class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp = 0
        for num in nums:
            temp ^= num
        return temp
