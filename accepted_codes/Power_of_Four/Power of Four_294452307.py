import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        if num <= 0 or num&1:
            return False
        root = int(math.sqrt(num))
        if root*root != num:
            return False
        return root&(root-1) == 0
