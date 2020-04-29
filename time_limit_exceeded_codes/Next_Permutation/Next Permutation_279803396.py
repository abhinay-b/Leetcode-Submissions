class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        idx = len(nums) - 1
        
        found = False
        while idx > 0:
            if nums[idx-1] < nums[idx]:
                nums[idx-1],nums[idx] = nums[idx], nums[idx-1]
                found = True
                break
        if found == False:
            nums = nums[::-1]
        
