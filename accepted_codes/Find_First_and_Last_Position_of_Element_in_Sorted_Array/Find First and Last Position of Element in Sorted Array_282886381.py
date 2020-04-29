import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = bisect.bisect_left(nums,target)
        if i != len(nums) and nums[i] == target:
            j = bisect.bisect_right(nums,target)
            if nums[j-1] == target:
                return[i,j-1]
        return[-1,-1]
