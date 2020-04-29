class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        def checkMin(numCoins,target,idx,minCoins):
            newCoins = target//coins[idx]
            if target % coins[idx] == 0:
                return min(numCoins+newCoins,minCoins)
            if idx == len(coins)-1:
                return minCoins
            for i in range(newCoins,-1,-1):
                produced = i*coins[idx]
                remaining = target - produced
                if numCoins+i+(remaining//coins[idx+1]) < minCoins:
                    minCoins=checkMin(numCoins+i,remaining,idx+1,minCoins)
            return minCoins
        coins.sort(reverse=True)
        minCoins = checkMin(0,amount,0,amount+1)
        return minCoins if minCoins < amount+1 else -1     
            
