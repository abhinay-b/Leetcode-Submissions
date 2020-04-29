class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def buildAll(ele,arr,left):
            if left == 0:
                res.append(ele)
                return
            for idx,item in enumerate(arr):
                buildAll(ele+[item],arr[idx+1:],left-1)
        if n < 2:
            return range(1,n+1)
        nums = [i for i in range(1,n+1)]
        res = []
        buildAll([],nums,k)
        return res
