class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0   
        if len(nums) == 1:
            return nums[0]
        maxVal = -float('inf')
        temp,negative,start = 1,1,-1
        for i in range(len(nums)):
            if nums[i] == 0:
                if start == -1 or i-1 == start:
                    maxVal = max(maxVal,0)
                else:
                    maxVal=max(maxVal,temp//negative)
                start = i
                negative = 1
                temp = 1
            else:
                temp = temp*nums[i]
                if temp < 0 and negative == 1:
                        negative = temp
                maxVal = max(maxVal,temp)
        if temp < 0 and start < len(nums)-2:
            maxVal = max(maxVal,temp//negative)
        return maxVal
