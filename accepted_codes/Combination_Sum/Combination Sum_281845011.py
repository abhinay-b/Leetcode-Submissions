class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        def combo(candidates,tempSum,tempList):
            for index,entry in enumerate(candidates):
                nxtSum = tempSum+entry
                if nxtSum < target:                    
                    tempList.append(entry)
                    combo(candidates[index:],nxtSum,tempList.copy())
                    tempList = tempList[:-1]
                elif nxtSum == target:
                    tempList.append(entry)
                    res.append(tempList)
                else:
                    break
        candidates.sort()
        temp = list()
        combo(candidates,0,temp.copy())
        return res
