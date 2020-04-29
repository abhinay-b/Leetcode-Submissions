class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        def combo(candidates,tempSum,tempList):
            for index,entry in enumerate(candidates):
                nxtSum = tempSum+entry
                if nxtSum < target:                    
                    tempList.append(entry)
                    combo(candidates[index+1:],nxtSum,tempList.copy())
                    tempList = tempList[:-1]
                elif nxtSum == target:
                    tempList.append(entry)
                    res.append(tempList)
                else:
                    break
        candidates.sort()
        temp = list()
        ctr = 0
        while ctr < len(candidates):
            temp = [candidates[ctr]]
            combo(candidates[ctr+1:],candidates[ctr],temp.copy())
            while ctr < len(candidates)-1 and candidates[ctr] == candidates[ctr+1]:
                ctr += 1
            ctr += 1
        return res
