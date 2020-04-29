class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        stack = []
        res = [-1]*len(nums)
        maxIdx = nums.index(max(nums))
        for idx in range(maxIdx+1,maxIdx+1+len(nums)):
            idx %= len(nums)
            while stack and nums[stack[-1]] < nums[idx]:
                res[stack[-1]] = nums[idx]
                stack.pop()
            stack.append(idx)
        return res
