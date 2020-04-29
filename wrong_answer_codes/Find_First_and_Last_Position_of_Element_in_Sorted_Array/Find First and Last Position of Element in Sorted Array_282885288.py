import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i,j = -1,0
        i = bisect.bisect_left(nums,target)
        if i != -1:
            j = bisect.bisect_right(nums,target)
        return[i,j-1]
