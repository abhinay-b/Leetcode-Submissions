class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        while(dividend >= divisor):
            count = 1
            temp = divisor
            while(dividend >= temp):
                temp <<= 1
                count <<= 1
            res += count >> 1
            dividend -= temp >> 1
        sign = (dividend < 0) ^ (divisor < 0)
        if sign == True:
            return -res
        else:
            return res
