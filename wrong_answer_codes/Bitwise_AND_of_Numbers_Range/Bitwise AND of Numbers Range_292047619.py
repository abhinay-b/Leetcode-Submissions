import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m==0:
            return 0
        if m == n:
            return m
        start = int(math.log(m,2))
        end = int(math.log(n,2))
        if start == end:
            return 2**start
        return 0
