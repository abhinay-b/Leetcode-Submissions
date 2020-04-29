from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        root = int(math.log(n,3))
        return 3**root == n
