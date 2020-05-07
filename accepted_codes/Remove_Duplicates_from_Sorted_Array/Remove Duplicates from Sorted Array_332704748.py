class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = idx = 0
        if len(nums) < 2:
            return len(nums)
        while idx < len(nums):
            if nums[length] != nums[idx]:
                length += 1
                nums[length] = nums[idx]
                
            idx += 1
            
        # print(nums)
        return length+1
