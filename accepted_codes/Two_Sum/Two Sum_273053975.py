class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        copy the list to a map
        numMap = dict()
        for index, element in enumerate(nums):
            if element not in numMap:
                numMap[element] = [index]
            else:
                numMap[element].append(index)
        print(numMap)
        for index, element in enumerate(nums):
            otherNum = target - element
            if otherNum in numMap:
                if otherNum != element:
                    return index, numMap[otherNum][0]
                elif otherNum == element and len(numMap[otherNum]) > 1:
                    return numMap[otherNum][0], numMap[otherNum][1]
                    
            
