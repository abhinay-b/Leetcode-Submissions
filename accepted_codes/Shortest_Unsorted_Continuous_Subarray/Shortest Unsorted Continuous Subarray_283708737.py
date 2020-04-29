class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        lidx,ridx = -1,-1
        if not nums:
            return 0
        i = 0
        while i < len(nums)-1:
            if nums[i] > nums[i+1]:
                lidx = ridx = i
                break
            i += 1
        maxElem = minElem = nums[i]
        while i < len(nums):
            if maxElem > nums[i]:
                ridx = i
            else:
                maxElem = nums[i]
            if minElem > nums[i]:
                minElem = nums[i]
            i += 1
            
        i = lidx - 1
        while i > -1:
            if minElem < nums[i]:
                lidx = i
            i -= 1
        # print(ridx,lidx)
        return len(nums[lidx:ridx+1])
