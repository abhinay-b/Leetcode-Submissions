class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for num in nums:
            count[num] += 1
        i = 0
        while i < len(nums):
            for idx in range(len(count)):
                while count[idx] > 0:
                    nums[i] = idx
                    count[idx] -= 1
                    i += 1
                    
