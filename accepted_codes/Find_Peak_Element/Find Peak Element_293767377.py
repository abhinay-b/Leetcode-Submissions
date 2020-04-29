class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Look for descending pair of neighbours every time
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        left,right = 0,len(nums)-1
        while left < right:
            mid = (left+right+1) // 2
            if nums[mid]-nums[mid-1] < 0:
                right = mid-1
            else:
                left = mid
        return left
