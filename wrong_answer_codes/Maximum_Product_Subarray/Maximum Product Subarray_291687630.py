class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0   
        if len(nums) == 1:
            return nums[0]
        maxVal = -float('inf')
        temp,negative = 1,1
        for i in range(len(nums)):
            if nums[i] == 0:
                maxVal=max(maxVal,temp//negative,0)
                negative = 1
                temp = 1
            else:
                temp = temp*nums[i]
                if temp < 0 and negative == 1:
                        negative = temp
                maxVal = max(maxVal,temp)
        if temp < 0:
            maxVal = max(maxVal,temp//negative)
        return maxVal
