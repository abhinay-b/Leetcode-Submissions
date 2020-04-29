class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        numCoins = [float('inf')]*(amount+1)
        numCoins[0] = 0
        for i in range(1,len(numCoins)):
            for j in range(len(coins)):
                if coins[j] <= i:
                    numCoins[i] = min(numCoins[i], 1+numCoins[i-coins[j]])
        if numCoins[-1] < float('inf'):
            return numCoins[-1]
        return -1
