import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        totalFac = math.factorial(n)
        if k > totalFac:
            return ""
        res = ""
        nums = [i for i in range(1,n+1)]
        for i in range(1,n+1):
            temp = (math.factorial(n-i))
            idx = k // temp
            k %= temp
            if k == 0:
                k = temp
                if idx > 0:
                    idx -= 1
            res += str(nums[idx])
            nums.pop(idx)
        return res
