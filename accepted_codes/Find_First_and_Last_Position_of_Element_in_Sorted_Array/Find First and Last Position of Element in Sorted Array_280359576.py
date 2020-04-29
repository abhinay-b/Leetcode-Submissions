class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        def search(nums,start,end):
            if start > end:
                return [-1,-1]
            mid = (start + end) // 2
            if nums[start] == target:
                mid = start
            elif nums[end] == target:
                mid = end
            if nums[mid] == target:
                l = r = mid
                while (l >= 0 and nums[l] == target ) or (r < len(nums) and nums[r] == 
                    target):
                    if l >= 0 and nums[l] == target:
                        l -= 1
                    if r < len(nums) and nums[r] == target:
                        r += 1
                return [l+1,r-1]
            if nums[mid] < target:
                return search(nums,mid+1,end)
            else:
                return search(nums,start,mid-1)

