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
        
        if idx > 0:
            nxtBig = nums[pos+1]
            curr = pos
            nums[curr+1:] = sorted(nums[curr+1:])
            idx = curr+1
            print(idx,curr)
            while idx < len(nums) and nums[curr] > nums[idx]:
                idx += 1
            nums[idx], nums[curr] = nums[curr], nums[idx]
            
        else:
            nums.reverse()
        # print(nums)
        
