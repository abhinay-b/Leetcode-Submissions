class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        copy the list to a map
        numMap = dict()
        for index, element in enumerate(nums):
            numMap[element] = index
        for index, element in enumerate(nums):
            otherNum = target - element
            if otherNum in numMap:
                return index, numMap[otherNum]
