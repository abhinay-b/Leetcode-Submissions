class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        idx = len(nums) - 1
        pos = 0
        while idx > 0:
            if nums[idx] > nums[idx-1]:
                pos = idx - 1
                break
            idx -= 1
        if idx > -1:
            nxtBig = nums[pos+1]
            curr = pos
            nums[curr+1:] = sorted(nums[curr+1:])
            nums[-1], nums[curr] = nums[curr], nums[-1]
            
        else:
            nums = nums[::-1]
        print(nums)
        
