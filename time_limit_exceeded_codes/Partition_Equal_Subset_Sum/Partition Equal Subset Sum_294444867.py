from collections import defaultdict
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True        
        # nums.sort(reverse=True)
        def helper(nums,current,target):
            for idx,num in enumerate(nums):
                if current+num > target:
                    return False
                if current+num == target:
                    return True
                if helper(nums[idx+1:],current+num,target):
                    return True
            return False
        target = sum(nums)
        if target&1:
            return False
        return helper(nums,0,sum(nums)/2)
