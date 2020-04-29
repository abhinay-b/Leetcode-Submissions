class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen and n != 1:
            seen.add(n)
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n //= 10
            n = res
        return n == 1
