class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        first,second = nums[0],nums[1]
        for i in range(2,len(nums)):
            if not i%2:
                second = max(first,second)
                first += nums[i]
            else:
                first = max(first,second)
                second += nums[i]
        return max(first,second)
                
