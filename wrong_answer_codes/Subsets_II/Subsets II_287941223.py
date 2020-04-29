class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def buildAll(temp,nums,k):
            if not nums or k < 1:
                res.append(temp)
                return
            i = 0
            while i < len(nums):
                buildAll(temp+[nums[i]],nums[i+1:],k-1)
                while i < len(nums)-1 and nums[i] == nums[i+1]:
                    i += 1
                i += 1
        nums.sort()
        res = [nums]
        for i in range(len(nums)):
            buildAll([],nums,i)
        return res
