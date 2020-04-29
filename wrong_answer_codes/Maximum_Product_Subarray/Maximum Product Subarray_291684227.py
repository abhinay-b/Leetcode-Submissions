class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0   
        if len(nums) == 1:
            return nums[0]
        maxVal = nums[0]
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
