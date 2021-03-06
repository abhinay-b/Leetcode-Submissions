class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Look for descending pair of neighbours every time
        left,right = 0,len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid]-nums[mid-1] < 0:
                right = mid
            else:
                left = mid+1
        return left-1
