class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        count = 0
        for i in range(len(coins)-1,-1,-1):
            count += amount // coins[i]
            amount %= coins[i]            
        if amount > 0:
            return -1
        return count
