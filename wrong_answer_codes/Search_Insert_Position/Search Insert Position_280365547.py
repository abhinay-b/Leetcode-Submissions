class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start,end = 0,len(nums)-1
        while(start+1 < end):
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] < target:
            return end
        else:
            return start
