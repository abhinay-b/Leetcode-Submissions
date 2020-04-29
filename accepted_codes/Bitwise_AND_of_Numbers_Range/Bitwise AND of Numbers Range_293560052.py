import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m*n == 0:
            return 0
        maxBit = math.floor(math.log(n,2))+1
        mask = 1
        setBit = 0
        for i in range(maxBit,-1,-1):
            mask = 1 << i
            if (m&mask) ^ (n&mask) != 0:
                if mask > m:
                    return 0
                else:
                    return setBit & m
            setBit |= mask
        return m
            
