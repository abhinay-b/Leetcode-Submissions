class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = idx = 0
        if len(nums) < 2:
            return len(nums)
        while idx < len(nums):
            while idx < len(nums) - 1 and nums[idx] == nums[idx+1]:
                idx += 1
            nums[length] = nums[idx]
            idx += 1
            length += 1
        # print(nums)
        return length
