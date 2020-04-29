class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        left,right = 0,len(prices)-1
        maxVal = 0
        while left < right:
            if prices[right] - prices[left] < 0 :
                left += 1
            else:
                maxVal = max(maxVal,prices[right]-prices[left])
                right -= 1
        return maxVal
