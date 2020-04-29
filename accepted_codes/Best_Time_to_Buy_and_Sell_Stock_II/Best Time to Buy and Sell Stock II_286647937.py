class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        for i in range(len(prices)-1):
            temp = prices[i+1] - prices[i]
            if temp > 0:
                profit += temp
        return profit
