class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        start,end = 0,len(nums)-1
        left,right = -1,-1
        while(start+1 < end):
            mid = (start + end)//2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid+1
        if nums[start] == target:
            left = start
        elif nums[end] == target:
            left = end
        
        start,end = 0,len(nums)-1
        while(start+1 < end):
            mid = (start+end)//2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid - 1
        if nums[end] == target:
            right = end
        elif nums[start] == target:
            right = start
        return [left,right]
        
