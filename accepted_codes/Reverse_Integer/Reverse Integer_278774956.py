class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < (-2 ** 31) or x >= (2 ** 31):
            return 0
        if x < 0:
            sign = -1
            x *= sign
        y = sign * int(str(x)[::-1])
        if y < (-2 ** 31) or y >= (2 ** 31):
            return 0
        return y
            
