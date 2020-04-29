class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        index = n-1
        for i in range(n-2,-1,-1):
            if nums[i] + i >= index:
                index = i
        if index == 0:
            return True
        return False
