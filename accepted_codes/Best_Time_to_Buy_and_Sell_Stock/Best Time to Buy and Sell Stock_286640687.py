class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minVal = prices[0]
        maxVal = 0
        for i in range(1,len(prices)):
            temp = prices[i] - minVal
            if temp < 0:
                minVal = prices[i]
            else:
                maxVal = max(maxVal,temp)
        return maxVal
