class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0        
        maxVal = -float('inf')
        temp,negative = 1,1
        for i in range(len(nums)):
            temp = temp*nums[i]
            if temp == 0:
                temp = nums[i]
            elif temp < 0 and negative == 1:
                    negative = temp
            maxVal = max(maxVal,temp)
        if temp < 0:
            maxVal = max(maxVal,temp//negative)
        return maxVal
