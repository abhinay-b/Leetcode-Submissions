class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        halfPower = self.myPow(x,n//2)
        halfPower *= halfPower
        if n%2 == 0:
            return halfPower
        return halfPower * x
