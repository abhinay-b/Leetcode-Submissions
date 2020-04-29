class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        def combo(candidates,tempSum,tempList):
            for index,entry in enumerate(candidates):
                nxtSum = tempSum+entry
                if nxtSum < target:                    
                    tempList+=str(entry)
                    combo(candidates[index:],nxtSum,tempList)
                    tempList = tempList[:-1]
                elif nxtSum == target:
                    tempList+=str(entry)
                    res.append(tempList)
                else:
                    break
        candidates.sort()
        temp = ""
        combo(candidates,0,temp)
        return [list(map(int,res[i])) for i in range(len(res))]
