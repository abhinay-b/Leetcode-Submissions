class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True        
        def Knapsack(weights,capacity):
            K = [[0]*(capacity+1) for _ in range(len(weights))]
            for i in range(len(weights)):
                for j in range(1,capacity+1):
                    K[i][j] = K[i-1][j]
                    if j >= weights[i]:
                        K[i][j] = max(K[i][j],K[i-1][j-weights[i]]+weights[i])
            return K[-1][-1] == capacity
        total = sum(nums)
        if total % 2:
            return False
        return Knapsack(nums,total//2)
