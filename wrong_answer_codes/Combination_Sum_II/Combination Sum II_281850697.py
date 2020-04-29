class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        res_set = set()
        def combo(candidates,tempSum,tempList,tempStr):
            for index,entry in enumerate(candidates):
                nxtSum = tempSum+entry
                if nxtSum < target:                    
                    tempList.append(entry)
                    tempStr += str(entry)
                    combo(candidates[index+1:],nxtSum,tempList.copy(),tempStr)
                    tempList = tempList[:-1]
                    tempStr = tempStr[:-1]
                elif nxtSum == target:
                    tempStr += str(entry)
                    if tempStr not in res_set:
                        tempList.append(entry)
                        res_set.add(tempStr)
                        res.append(tempList)
                else:
                    break
        candidates.sort()
        temp = list()
        tempStr = ""
        combo(candidates,0,temp.copy(),tempStr)
        return res
