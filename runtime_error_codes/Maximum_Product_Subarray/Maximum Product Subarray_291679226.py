class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = -float('inf')
        start,temp,negative = -1,1,0
        for i in range(len(nums)):
            if temp == 0:
                temp = nums[i]
            else:
                if temp < 0:
                    start = i-1
                    negative = temp
                temp = temp*nums[i]
            maxVal = max(maxVal,temp)
        if negative == temp:
            maxVal = max(maxVal,temp//nums[start])
        elif temp < 0:
            maxVal = max(maxVal,temp//negative)
        return maxVal
