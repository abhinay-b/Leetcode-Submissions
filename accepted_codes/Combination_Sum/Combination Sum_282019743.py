class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        def combo(candidates,tempSum,tempList):
            for index,entry in enumerate(candidates):
                nxtSum = tempSum+entry
                if nxtSum < target:                    
                    combo(candidates[index:],nxtSum,tempList+[entry])
                elif nxtSum == target:
                    res.append(tempList+[entry])
                else:
                    break
        candidates.sort()
        temp = list()
        combo(candidates,0,temp)
        return res
