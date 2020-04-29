import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while(left < right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    return bisect.bisect(nums,target,left,mid)-1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    return bisect.bisect(nums,target,mid,right)-1
                else:
                    right = mid
        return bisect.bisect(nums,target,left,right)-1
