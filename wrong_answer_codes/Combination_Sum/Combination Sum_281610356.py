class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res = []
        def combo(candidates,tempSum,tempList):
            for index,entry in enumerate(candidates):
                tempSum += entry
                if tempSum < target:
                    tempList.append(entry)
                    combo(candidates[index:],tempSum,tempList.copy())
                elif tempSum == target:
                    tempList.append(entry)
                    res.append(tempList)
                else:
                    break
        candidates.sort()
        temp = list()
        for index in range(len(candidates)):
            combo(candidates[index:],0,temp.copy())
        return res
