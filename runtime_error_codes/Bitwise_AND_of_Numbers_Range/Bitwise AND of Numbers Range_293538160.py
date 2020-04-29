import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        diff = n-m
        shift = math.ceil(math.log(diff))+1
        if diff:
            return (n >> shift) << shift
        return n
