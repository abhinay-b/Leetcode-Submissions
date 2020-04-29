import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m*n == 0:
            return 0
        diff = n-m
        logN = int(math.floor(math.log(n,2)))
        logM = int(math.floor(math.log(m,2)))
        shift = logN - logM
        if shift:
            return 0
        if diff:
            shift = int(math.floor(math.log(diff,2)))+1
            return (m >> shift) << shift
        return n
