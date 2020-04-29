from math import log,ceil
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        root = ceil(log(n,3))
        return 3**root == n
