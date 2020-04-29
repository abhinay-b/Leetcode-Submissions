class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        temp = [0]*(n+1)
        temp[0] = temp[1] = 1
        for i in range(2,n+1):
            temp[i] = temp[i-1] + temp[i-2]
        return temp[n]
