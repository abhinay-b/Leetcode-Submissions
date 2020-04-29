class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        while left<right:
            sumVal = numbers[left]+numbers[right]
            if sumVal == target:
                return [left+1,right+1]
            if sumVal > 0:
                right -= 1
            if sumVal < 0:
                left += 1
        return [-1,-1]
