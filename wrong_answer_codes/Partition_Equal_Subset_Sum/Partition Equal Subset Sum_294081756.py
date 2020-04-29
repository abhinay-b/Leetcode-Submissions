class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        nums.sort()
        total = sum(nums)
        if total % 2:
            return False
        mid = total/2
        count = 0
        i = 0
        while count < mid:
            count += nums[i]
            i += 1
        return mid == sum(nums[i:])
