class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= sign
        return sign * int(str(x)[::-1])
            
