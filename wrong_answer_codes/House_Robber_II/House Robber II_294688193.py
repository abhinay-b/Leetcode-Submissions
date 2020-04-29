class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            idxVal = [nums[0], nums[1]]
            length = len(nums)
            for i in range(2,length):
                temp = max(idxVal[0],idxVal[1])
                idxVal[i%2] += nums[i]
                idxVal[((i%2)+1)%2] = temp
            return max(idxVal)
        return max(helper(nums[:-1]),helper(nums[1:]))
