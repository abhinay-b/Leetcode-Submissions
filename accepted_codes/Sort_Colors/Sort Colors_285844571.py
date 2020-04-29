class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ridx,bidx = 0, len(nums)-1
        i = 0
        while i < len(nums): 
            if nums[i] == 0:
                nums[ridx],nums[i] = nums[i],nums[ridx]
                ridx += 1
                i += 1
            elif nums[i] == 2:
                nums[bidx],nums[i] = nums[i],nums[bidx]
                bidx -= 1
            else:
                i += 1
            if i > bidx:
                break
