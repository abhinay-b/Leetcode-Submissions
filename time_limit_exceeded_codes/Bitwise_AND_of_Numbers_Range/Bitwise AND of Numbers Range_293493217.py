from functools import reduce
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        nums = range(m,n+1)
        return reduce(lambda x,y:x&y,nums)
