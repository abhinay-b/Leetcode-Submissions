class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left,right = 0,len(nums)-1
        mid = (left+right) // 2
        while left < right and nums[left] == nums[right] == nums[mid]:
            left += 1
            right -= 1
        while left < right:            
            mid = (left+right)//2
            if nums[left] >= nums[right]:
                if nums[mid] <= nums[right]:
                    right = mid
                else:
                    left = mid+1
            else:
                return nums[left]
        return nums[left]
