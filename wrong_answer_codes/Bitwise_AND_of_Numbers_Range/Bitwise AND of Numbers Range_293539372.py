import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        diff = n-m        
        if diff:
            shift = int(math.ceil(math.log(diff,2)))+1
            return (m >> shift) << shift
        return n
