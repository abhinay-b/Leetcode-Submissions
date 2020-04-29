class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def buildAll(ele,arr,left):
            if left == 0:
                res.append(ele)
                return
            for idx,item in enumerate(arr):
                buildAll(ele+[item],arr[idx+1:],left-1)
        res = [nums]
        for k in range(len(nums)):
            buildAll([],nums,k)
        return res
        
