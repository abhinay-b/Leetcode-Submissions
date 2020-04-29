class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def buildAll(temp,nums,k):
            if not nums or k < 0:
                res.add(tuple((temp)))
                return
            for idx,num in enumerate(nums):
                buildAll(temp+[num],nums[idx+1:],k-1)
        res = {()}
        nums.sort()
        for i in range(len(nums)):
            buildAll([],nums,i)
        return res
