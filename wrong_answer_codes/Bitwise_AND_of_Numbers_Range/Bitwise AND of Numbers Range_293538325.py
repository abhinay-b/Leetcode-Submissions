import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        diff = n-m        
        if diff:
            shift = math.ceil(math.log(diff))+1
            return (n >> shift) << shift
        return n
