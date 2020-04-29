class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        def combo(candidates,tempSum,tempList):
            index = 0
            while index < len(candidates):
                entry = candidates[index]
                nxtSum = tempSum+entry                
                if nxtSum < target:                    
                    combo(candidates[index+1:],nxtSum,tempList+[entry])
                    while index < len(candidates)-1 and candidates[index] == candidates[index
                        +1]:
                        index += 1
                elif nxtSum == target:
                    res.append(tempList+[entry])
                    break
                else:
                    break
                index += 1
        candidates.sort()
        temp = list()
        combo(candidates,0,temp)
        return res
