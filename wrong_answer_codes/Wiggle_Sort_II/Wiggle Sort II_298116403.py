class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        for i in range(1,len(nums),2):
            if nums[i] < nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
            if i < len(nums)-1 and nums[i] < nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]
        
